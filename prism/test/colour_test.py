#!/usr/bin/env python -u
# encoding: utf-8
#
# Copyright (c) 2012, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under 3-clause BSD license.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

import pytest
from prism.colour import code, colour, colourcode

@pytest.mark.parametrize(("code", "name"), [
    # invalid
    ['', None],
    ['', ''],
    ['', 'invalid'],
    ['', 'bright invalid'],
    # valid
    [30, 'BLACK'],
    [31, 'red'],
    # ...
    [37, 'white'],
    # bright
    [91, 'BRIGHT RED'],
    [96, 'foo bright cyan red bar'],
])
def test_colourcode(code, name):
    assert code == colourcode(name)
    assert code + 10 if isinstance(code, int) else '' == colourcode(name, back=True)

def test_colour():
    assert '\x1b[31;m' == colour('RED')

