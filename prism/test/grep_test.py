#!/usr/bin/env python -u
#
# Copyright (c) 2012, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under 3-clause BSD license.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

from prism.grep import pattern, search


def log_lines():
    return [
        "[Sun Apr 08 12:51:52 2012] [notice] Digest: done",
        "[Mon Jul 11 09:26:13 2011] Error: [client ::1]"
        + "File does not exist: /Library/WebServer/Documents/favicon.ico",
    ]


def test_search():
    msg = "Regexp pattern '{0}' didn't match line '{1}'"
    for line in log_lines():
        assert search(line), msg.format(pattern, line)
