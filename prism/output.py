#!/usr/bin/env python -u
# encoding: utf-8
#
# Copyright (c) 2012, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under 3-clause BSD license.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

import fileinput
import os
import sys
import time

from prism import config
from prism.events import PrismEventHandler
from prism.log import log
from prism.grep import colourise

try:
    from watchdog.observers import Observer
    use_watchdog = True
except ImportError as e:
    use_watchdog = False

# Unbuffered I/O not allowed on Python 3
# See http://bugs.python.org/issue11633 for conversation
if sys.version_info <= (3, 0) and type(sys.stdout) == 'file':
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

def outputlines(fi, grep=False, match_only=False, watch=True):
    try:
        if watch and (fi == '-' or fi == sys.stdin):
            fi = sys.stdin
            while 1:
                try:
                    sys.stdout.write(colourise(fi.readline(), grep, match_only))
                except KeyboardInterrupt:
                    break
        else:
            for line in fi:
                if fi.isstdin():
                    sys.stdout.write(colourise(line, grep, match_only))
                else:
                    sys.stdout.write(colourise(line, grep, match_only))
    except IOError as e:
        log.error(e)
        quit()

def tail_generator(fi, grep=False, match_only=False):
    while 1:
        try:
            line = fi.readline()
            if not line:
                time.sleep(0.00125)
                continue
            yield colourise(line.rstrip(), grep, match_only)
        except KeyboardInterrupt:
            fi.close()
            quit()

def tail():
    """Simple tail -f like function, that will wait for input"""

    log.info("Using TAIL. Press ^C to quit. For help, see 'prism -h'.")
    gen = tail_generator(
        fileinput.input(sys.argv, bufsize = config.buffer_size),
        grep = config.grep_opt,
        match_only = config.match_opt
    )
    while 1:
        print(next(gen))

def watch_output(event):
    print(("\n==> %s <==" % os.path.basename(event.src_path)))
    outputlines(fileinput.input(event.src_path), grep=config.grep_opt, match_only=config.match_opt)

def watch():
    fi = fileinput.input(sys.argv[1:], bufsize = config.buffer_size)
    paths = fi._files
    log.info("Using FILEINPUT with WATCHDOG for files: %s" % (', '.join(paths),))

    log.debug("Buffer size: %s" % fi._bufsize)

    event_handler = PrismEventHandler([os.path.abspath(p) for p in paths], watch_output)

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

