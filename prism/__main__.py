#!/usr/bin/env python -u
# encoding: utf-8
#
# Copyright (c) 2012, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under 3-clause BSD license.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

# Prism module colourises log files with ANSI character codes.

from __future__ import print_function

import fileinput
from itertools import izip

import config
import exceptions
import logging
import os
import sys
import time

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

from ansi import code, colour
from events import PrismEventHandler
from output import log, outputlines


def usage():
    return \
"""USAGE

Options:
---------
-g   show only matched lines (like grep)
-m   only colour matched parts of lines (default: colourise whole line)
-w   use watchdog to monitor for changes (acts like tail -f)

-h   this help
-d   enable debug logging

Examples:
---------
# Multiple files
prism *.log

# Watching mode
tail -f /var/log/system.log | prism
tail -f /var/log/system.log | prism -

# Watch a directory with watchdog
prism -w .

Credits:
--------
Copyright (c) 2012, Peter Hillerström
Homepage: https://github.com/peterhil/prism"""
__doc__ = usage()

def prism_logo():
    res = ''
    for c, letter in izip('rygcb', 'PRISM'):
        res += '{0} {1} '.format(colour(c, 'bright ' + c), letter)
    return res + code(0)

def nameplate():
    return "\n {0}\n  {1} coloured logs \n{2}".format(prism_logo(), code(7), code(0))


if __name__ in ['__main__', 'prism']:
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    buffer_size = 1

    log.info(nameplate())

    config.grep_opt = False
    config.match_opt = False

    if len(sys.argv) > 1:
        if '-h' in sys.argv:
            log.info(usage() + "\n")
            quit()
        if '-d' in sys.argv:
            log.setLevel(logging.DEBUG)
            sys.argv.pop(sys.argv.index('-d'))
        if '-m' in sys.argv:
            config.match_opt = True
            sys.argv.pop(sys.argv.index('-m'))
        if '-g' in sys.argv:
            config.grep_opt = True
            sys.argv.pop(sys.argv.index('-g'))

    log.debug("Processed args: %s" % sys.argv)

    if len(sys.argv) == 1 or len(sys.argv) == 2 and sys.argv[1] == '-':
        log.info("Using STDIN. Press ^C to quit. For help, see 'prism -h'.")
        outputlines(sys.stdin, grep = config.grep_opt, match_only = config.match_opt)
    elif len(sys.argv) > 1 and sys.argv[1] == '-w':
        sys.argv.pop(1)

        fi = fileinput.input(sys.argv[1:], bufsize = buffer_size)
        paths = fi._files
        log.info("Using FILEINPUT with WATCHDOG for files: %s" % (', '.join(paths),))

        log.debug("Buffer size: %s" % fi._bufsize)

        event_handler = PrismEventHandler(map(lambda p: os.path.abspath(p), paths))

        observer = Observer()
        recursive = False

        for p in paths:
            if p == '-' or p == sys.stdin:
                log.error("Can't mix stdin with file arguments. Quitting.")
                quit()
            else:
                if os.path.isdir(p):
                    log.info("Watching directory '%s'" % p)
                    recursive = True
                else:
                    log.info("Will schedule file '%s'" % p)
                    recursive = False
                p = os.path.dirname(os.path.abspath(p)) # Watchdog doesn't notify of file changes?
                observer.schedule(event_handler, path=p, recursive=recursive)

        observer.start()
        try:
            while True:
                time.sleep(0.125)
        except KeyboardInterrupt:
            observer.stop()
            quit()
        observer.join()
    else:
        log.info("Using fileinput.")
        outputlines(fileinput.input(sys.argv[1:], bufsize = buffer_size), grep = config.grep_opt, match_only = config.match_opt)
