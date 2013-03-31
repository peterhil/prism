#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2012, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under 3-clause BSD license.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

import sys

if sys.version_info >= (2, 7, 0):
    from collections import OrderedDict as od
else:
    from ordereddict import OrderedDict as od

__all__ = ['level_map', 'options']

class options(object):
    use_watchdog = False
    buffer_size = 1
    grep_opt = False
    match_opt = False
    tail_opt = False

level_map = od([
    ('emerg',           ['black', 'bright red']),
    ('alert',           ['black', 'bright red']),
    ('critical',        ['black', 'bright red']),
    ('crit',            ['black', 'bright red']),
    ('fatal error',     ['black', 'bright red']),
    ('fatal',           ['black', 'bright red']),
    ('failure',         ['black', 'bright red']),
    ('fail',            ['black', 'bright red']),

    ('parse error',     ['bright red']),
    ('error',           ['bright red']),

    ('warning',         ['bright yellow']),
    ('warn',            ['bright yellow']),

    # HTTP methods
    ('post',            ['bright red', 'red']),
    ('delete',          ['bright red', 'red']),
    ('put',             ['bright yellow', 'yellow']),
    ('patch',           ['bright yellow', 'yellow']),
    ('update',          ['bright green', ' yellow']),
    ('get',             ['bright cyan', 'cyan']),
    ('head',            ['bright green', 'green']),

    # SQL logs
    ('drop',            ['black', 'bright red']),
    ('alter',           ['bright red']),
    ('create',          ['bright yellow']),
    ('insert',          ['bright green']),
    ('pragma',          ['bright magenta']),
    ('select',          ['bright cyan']),

    ('failed',          ['bright yellow']),
    ('invalid',         ['bright yellow']),

    ('notice',          ['bright green']),
    ('note',            ['bright green']),

    ('info',            ['bright cyan']),

    ('debug',           ['bright magenta']),

    ('dribble',         ['bright black']),
])

