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


from prism.config import options
from prism.log import log
from prism.grep import colourise

if options.use_watchdog:
    from watchdog.observers import Observer
    from prism.events import PrismEventHandler


def outputlines(fi, grep=False, match_only=False, watch=True):
    try:
        if watch and (fi == "-" or fi == sys.stdin):
            fi = sys.stdin
            while 1:
                try:
                    line = fi.readline()
                    if line:
                        sys.stdout.write(colourise(line, grep, match_only))
                except KeyboardInterrupt:
                    break
        else:
            for line in fi:
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
        fileinput.input(sys.argv[1:]),
        grep=options.grep_opt,
        match_only=options.match_opt,
    )
    while 1:
        print(next(gen))


def watch_output(event):
    print(("\n==> %s <==" % os.path.basename(event.src_path)))
    outputlines(
        fileinput.input(event.src_path),
        grep=options.grep_opt,
        match_only=options.match_opt,
    )


def watch():
    if not options.use_watchdog:
        log.error("Watchdog not installed.")
        quit()

    fi = fileinput.input(sys.argv[1:])
    paths = fi._files

    msg = "Using FILEINPUT with WATCHDOG for files: %s"
    log.info(msg % (", ".join(paths),))

    abs_paths = [os.path.abspath(p) for p in paths]
    event_handler = PrismEventHandler(abs_paths, watch_output)
    observer = Observer()
    recursive = False

    for p in paths:
        if p == "-" or p == sys.stdin:
            log.error("Can't mix stdin with file arguments. Quitting.")
            quit()
        else:
            if os.path.isdir(p):
                log.info("Watching directory '%s'" % p)
                recursive = True
            else:
                log.info("Will schedule file '%s'" % p)
                recursive = False
            p = os.path.dirname(
                os.path.abspath(p)
            )  # Watchdog doesn't notify of file changes?
            observer.schedule(event_handler, path=p, recursive=recursive)

    observer.start()
    try:
        while True:
            time.sleep(0.125)
    except KeyboardInterrupt:
        observer.stop()
        quit()
    observer.join()
