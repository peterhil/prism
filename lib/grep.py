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

import re

from .ansi import *
from .config import config


pattern = re.compile(r'[ \[\":](' + \
	r'|'.join(config.keys()) + \
	r')[ \]:]', flags=re.I)


def search(line):
	return re.findall(pattern, line)

def colourise(line):
	m = search(line)
	if m:
		c = 0
		for level in config.keys():
			if level in m:
				c = config[level]
				break
		return colour(c) + line + code(0)
	else:
		return line
