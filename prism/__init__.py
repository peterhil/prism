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

import fileinput
from itertools import izip

from .ansi import *
from .config import config
from .grep import *

__doc__ = """
Usage
=====

tail -f /var/log/system.log | prism -f ~/.prism.conf
"""


def prism():
	res = ''
	colours = 'rrryyygggcccbbb'
	string =  ' P  R  I  S  M '
	for c, s in izip(colours, string):
		res += colour(c, 'bright ' + c) + s
	return res + code(0)

def nameplate():
	return "\n" + colour('bright white') + " " + prism() + code(1) + "\n " + \
	       " " + code(7) + " coloured logs " + "\n" + code(0)

def usage():
	return __doc__

