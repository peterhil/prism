#!/usr/bin/env python -u
#
# Copyright (c) 2012, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under 3-clause BSD license.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

__all__ = ["level_map", "options"]


from collections import OrderedDict as od


class options:
    grep_opt = False
    match_opt = False
    tail_opt = False
    watch_opt = False


level_map = od(
    [
        ("emerg", ["black", "bright red"]),
        ("alert", ["black", "bright red"]),
        ("critical", ["black", "bright red"]),
        ("crit", ["black", "bright red"]),
        ("fatal error", ["black", "bright red"]),
        ("fatal", ["black", "bright red"]),
        ("failure", ["black", "bright red"]),
        ("fail", ["black", "bright red"]),
        ("parse error", ["bright red"]),
        ("error", ["bright red"]),
        ("warning", ["bright yellow"]),
        ("warn", ["bright yellow"]),
        # HTTP methods
        ("post", ["bright red", "red"]),
        ("delete", ["bright red", "red"]),
        ("put", ["bright yellow", "yellow"]),
        ("patch", ["bright yellow", "yellow"]),
        ("update", ["bright green", " yellow"]),
        ("get", ["bright cyan", "cyan"]),
        ("head", ["bright green", "green"]),
        # SQL logs
        ("drop", ["black", "bright red"]),
        ("alter", ["bright red"]),
        ("create", ["bright yellow"]),
        ("insert", ["bright green"]),
        ("pragma", ["bright magenta"]),
        ("select", ["bright cyan"]),
        ("failed", ["bright yellow"]),
        ("invalid", ["bright yellow"]),
        ("notice", ["bright green"]),
        ("note", ["bright green"]),
        ("info", ["bright cyan"]),
        ("debug", ["bright magenta"]),
        ("dribble", ["bright black"]),
    ]
)
