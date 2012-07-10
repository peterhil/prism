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
sys.path.append('../lib/')

from lib import *

if __name__ != '__main__':
	__name__ = 'prism'

if __name__ in ['__main__', 'prism']:
	print nameplate()
	for line in fileinput.input():
		print colourise(line.rstrip())