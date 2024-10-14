#!/usr/bin/env python -u
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

from prism.events import PrismEventHandler
from prism.log import log
from prism.grep import colourise

from watchdog.observers import Observer


def outputlines(fi, grep=False, matches=False, watch=True):
    try:
        if watch and (fi == "-" or fi == sys.stdin):
            fi = sys.stdin
            while 1:
                try:
                    if line := fi.readline():
                        sys.stdout.write(colourise(line, grep, matches))
                except KeyboardInterrupt:
                    break
        else:
            for line in fi:
                sys.stdout.write(colourise(line, grep, matches))
    except OSError as e:
        log.error(e)
        quit()
    finally:
        fi.close()


def get_watch_handler(grep=False, matches=False):
    def watch_callback(event):
        print("\n==> %s <==" % os.path.basename(event.src_path))
        outputlines(
            fileinput.input(event.src_path),
            grep=grep,
            matches=matches,
        )

    return watch_callback


def watch_output(inputs, grep=False, matches=False):
    fi = fileinput.input(inputs)
    paths = fi._files

    msg = "Using FILEINPUT with WATCHDOG for files: %s"
    log.info(msg % (", ".join(paths),))

    abs_paths = [os.path.abspath(p) for p in paths]
    event_handler = PrismEventHandler(abs_paths, get_watch_handler(grep, matches))
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
    finally:
        fi.close()
    observer.join()
