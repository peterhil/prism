#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2012, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under 3-clause BSD license.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

# This module generates ANSI character codes for terminals.
# See: http://en.wikipedia.org/wiki/ANSI_escape_code#CSI_codes

import sys

if sys.version_info >= (2, 7, 0):
    from collections import OrderedDict as od
else:
    from ordereddict import OrderedDict as od

__all__ = ['level_map']


level_map = od([
    ('fatal',           'red'),
    ('critical',        'red'),
    ('failure',         'red'),
    ('fail',            'red'),
    ('fatal',           'red'),
    ('fatal error',     'red'),

    ('error',           'bright red'),
    ('parse error',     'bright red'),

    ('warning',         'bright yellow'),
    ('warn',            'bright yellow'),

    # HTTP methods
    ('post',            'bright red'),
    ('delete',          'bright red'),
    ('update',          'bright yellow'),
    ('put',             'bright yellow'),
    ('patch',           'bright yellow'),
    ('get',             'bright green'),
    ('head',            'bright cyan'),

    ('notice',          'bright green'),
    ('note',            'bright green'),

    ('info',            'bright cyan'),

    ('debug',           'bright magenta'),

    ('dribble',         'bright black'),
])
