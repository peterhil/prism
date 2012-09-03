#!/usr/bin/env python -u
# encoding: utf-8
#
# Copyright (c) 2012, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under 3-clause BSD license.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

import fileinput
import logging
import sys
import time
from grep import colourise

log = logging.getLogger('Prism')
log.addHandler(logging.StreamHandler(sys.stderr))
log.setLevel(logging.INFO)

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
    except IOError, e:
        log.error(e)
        quit()

def tail(fi, grep=False, match_only=False):
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
