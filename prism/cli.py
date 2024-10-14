#!/usr/bin/env python -u
#
# Copyright (c) 2012, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under 3-clause BSD license.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

"""Prism – colourise log levels and other keys on log files (with ANSI characters codes)"""

__all__ = ["main"]

import argh
import fileinput
import logging
import sys

from argh.decorators import arg

from prism.colour import prism_logo
from prism.output import log, outputlines, watch_output
from prism.__version__ import __version__


@arg("--debug", help="enable debug logging")
@arg("--grep", help="show only matched lines")
@arg("--matches", help="only colour matched parts of lines")
@arg("--watch", help="use watchdog to monitor for changes")
def command(
    *inputs,
    grep=False,
    matches=False,
    watch=False,
    debug=False,
):
    if debug:
        log.setLevel(logging.DEBUG)
        log.debug(f"Processed args: {sys.argv}, inputs: {inputs}")

    if watch:
        watch_output(inputs, grep, matches)
    elif not inputs or inputs == ["-"]:
        log.info("Using STDIN. Press ^C to quit. For help, see 'prism -h'.")
        outputlines(sys.stdin, grep, matches)
    else:
        log.info("Using fileinput.")
        fi = fileinput.input(inputs)
        outputlines(fi, grep, matches)


def main():
    log.info(prism_logo("version: " + __version__))
    argh.dispatch_command(command, always_flush=True)


if __name__ == "__main__":
    main()
