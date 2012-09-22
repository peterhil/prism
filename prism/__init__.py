#!/usr/bin/env python -u
# -*- coding: utf-8 -*-
#
# Copyright (c) 2012, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under 3-clause BSD license.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

from __future__ import print_function

import fileinput
import logging
import os
import sys

from prism import config
from prism.colour import prism_logo
from prism.output import log, outputlines, tail, watch

try:
    __import__('watchdog')
    use_watchdog = True
except ImportError as e:
    use_watchdog = False

__all__ = ['usage', 'main']
__doc__ = """Prism – colourise log levels and other keys on log files (with ANSI characters codes)

USAGE

Options:
---------
-g   show only matched lines (like grep)
-m   only colour matched parts of lines (default: colourise whole line)""" + \
("-w   use watchdog to monitor for changes (acts like tail -f)" if use_watchdog else "") + \
"""
-t   use tail function (use 'prism -t test.log' instead of 'tail -f test.log | prism')

-h   this help
-d   enable debug logging

Examples:
---------
# Multiple files
prism *.log

# Watching mode
tail -f /var/log/system.log | prism
tail -f /var/log/system.log | prism -
""" + \
("""
# Watch a directory with watchdog
prism -w .
""" if use_watchdog else "") + \
"""
Credits:
--------
Copyright (c) 2012, Peter Hillerström
Homepage: https://github.com/peterhil/prism
"""
 
def usage():
    return __doc__

def main():
    log.info(prism_logo())

    config.buffer_size = 1
    config.grep_opt = False
    config.match_opt = False
    config.tail_opt = False

    if len(sys.argv) > 1:
        if '-h' in sys.argv:
            log.info(usage())
            quit()
        if '-d' in sys.argv:
            log.setLevel(logging.DEBUG)
            sys.argv.pop(sys.argv.index('-d'))
        if '-t' in sys.argv:
            config.tail_opt = True
            sys.argv.pop(sys.argv.index('-t'))
        if '-m' in sys.argv:
            config.match_opt = True
            sys.argv.pop(sys.argv.index('-m'))
        if '-g' in sys.argv:
            config.grep_opt = True
            sys.argv.pop(sys.argv.index('-g'))

    log.debug("Processed args: %s" % sys.argv)

    if config.tail_opt:
        tail()
    elif len(sys.argv) == 1 or len(sys.argv) == 2 and sys.argv[1] == '-':
        log.info("Using STDIN. Press ^C to quit. For help, see 'prism -h'.")
        outputlines(sys.stdin, grep = config.grep_opt, match_only = config.match_opt)
    elif use_watchdog and len(sys.argv) > 1 and sys.argv[1] == '-w':
        sys.argv.pop(1)
        watch()
    else:
        log.info("Using fileinput.")
        fi = fileinput.input(sys.argv[1:], bufsize = config.buffer_size)
        outputlines(fi, grep = config.grep_opt, match_only = config.match_opt)

