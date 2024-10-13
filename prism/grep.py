#!/usr/bin/env python -u
# encoding: utf-8
#
# Copyright (c) 2012, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under 3-clause BSD license.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

import re

from prism.colour import colour, code
from prism.config import level_map

pattern = (
    r""" # Starting characters
(?:
^     |  # Start of line
[:\[] |  # One of: |:[|
(?<=     # Non-capturing group
  [ \"\'=\.]  # One of: | "'=.|
)
)
"""
    + r"("
    + r"|".join(list(level_map.keys()))
    + r")"
    + r"""  # Ending characters
    (?:      # Non-capturing group
    [:\]] |  # One of: |:]|
    $     |  # End of line
      (?=
        [ \"\'=]  # One of: | "'=|
      )
    )
"""
)

re_pattern = re.compile(pattern, flags=re.UNICODE | re.IGNORECASE | re.VERBOSE)


def search(line):
    return re.findall(re_pattern, line)


def colourise(line, grep=False, match_only=True):
    m = search(line)
    if m:
        s = [s.lower() for s in m]
        colour_name = 0

        if match_only:
            matches = re.finditer(re_pattern, line)
            for m in reversed(list(matches)):
                if m.group(1).lower() in list(level_map.keys()):
                    colour_name = level_map[m.group(1).lower()]
                line = (
                    line[0 : m.start()]  # noqa: E203
                    + colour(*colour_name)
                    + line[m.start() : m.end()]  # noqa: E203
                    + code(0)
                    + line[m.end() : len(line)]  # noqa: E203
                    + code(0)
                )
            return line
        else:
            for level in list(level_map.keys()):
                if level in s:
                    colour_name = level_map[level]
                    break
            return colour(*colour_name) + line + code(0)
    else:
        return "" if grep else line
