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

from itertools import ifilter


__all__ = [
	'code',
	'colourcode',
	'colour'
]


CSI = '\x1b['

COLOUR = {
    'black'   : 0,
    'red'     : 1,
    'green'   : 2,
    'yellow'  : 3,

    'blue'    : 4,
    'magenta' : 5,
    'cyan'    : 6,
    'white'   : 7,

    'k': 0,
    'r': 1,
    'g': 2,
    'y': 3,

    'b': 4,
    'm': 5,
    'c': 6,
    'w': 7,
    }

# Offsets
FORE = 30
BACK = 40
BRIGHT = 60

def code(code, op='m'):
    return CSI + str(code) + op

def colourcode(name, back=False):
	"""
	Return ANSI colour code for a colour name.
	If 'back' is True, returns a background colour.
	"""
	parts = str(name).lower().split()
	bright = BRIGHT * int('bright' in parts)

	try:
		colourname = next(ifilter(lambda s: s in COLOUR, parts), None)
	except StopIteration:
		pass

	if isinstance(COLOUR.get(colourname), int):
		colour = COLOUR.get(colourname) + (BACK if back else FORE)
		code = bright + colour
	else:
		code = ''

	return code

def colour(fore='', back=''):
	return CSI + str(colourcode(fore)) + ';' + str(colourcode(back, back=True)) + 'm'
