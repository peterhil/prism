#!/usr/bin/env python -u
#
# Copyright (c) 2012, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under 3-clause BSD license.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.


__all__ = ["usage", "main"]

import fileinput
import logging
import sys

from prism.colour import prism_logo
from prism.config import options
from prism.output import log, outputlines, tail, watch
from prism.__version__ import __version__

__doc__ = """Prism – colourise log levels and other keys on log files (with ANSI characters codes)

USAGE

Options:
---------
-g   show only matched lines (like grep)
-m   only colour matched parts of lines (default: colourise whole line)
-w   use watchdog to monitor for changes (acts like tail -f)
-t   use tail function (use 'prism -t test.log' instead of 'tail -f test.log | prism')  # noqa: E501

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
Homepage: https://github.com/peterhil/prism
"""


def usage():
    return __doc__


def main():
    log.info(prism_logo("version: " + __version__))

    if len(sys.argv) > 1:
        if "-h" in sys.argv:
            log.info(usage())
            quit()
        if "-d" in sys.argv:
            log.setLevel(logging.DEBUG)
            sys.argv.pop(sys.argv.index("-d"))
        if "-t" in sys.argv:
            options.tail_opt = True
            sys.argv.pop(sys.argv.index("-t"))
        if "-m" in sys.argv:
            options.match_opt = True
            sys.argv.pop(sys.argv.index("-m"))
        if "-g" in sys.argv:
            options.grep_opt = True
            sys.argv.pop(sys.argv.index("-g"))
        if "-w" in sys.argv:
            options.watch_opt = True
            sys.argv.pop(sys.argv.index("-w"))

    log.debug("Processed args: %s" % sys.argv)
    opts = dict(
        grep=options.grep_opt,
        match_only=options.match_opt,
    )

    if options.watch_opt:
        watch()

    elif options.tail_opt:
        tail()

    elif len(sys.argv) == 1 or len(sys.argv) == 2 and sys.argv[1] == "-":
        log.info("Using STDIN. Press ^C to quit. For help, see 'prism -h'.")
        outputlines(sys.stdin, **opts)

    else:
        log.info("Using fileinput.")
        fi = fileinput.input(sys.argv[1:])
        outputlines(fi, **opts)

    sys.stdout.flush()
