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

if sys.version > '2.7.0':
	from collections import OrderedDict as od
else:
	from ordereddict import OrderedDict as od


config = od([
	('fatal' 		, 'red'),
	('critical' 	, 'red'),
	('failure'		, 'red'),
	('error'		, 'bright red'),
	('POST'			, 'bright red'),
	('DELETE'		, 'bright red'),
	('warning'		, 'bright yellow'),
	('warn'			, 'bright yellow'),
	('UPDATE'		, 'bright yellow'),
	('notice'		, 'bright green'),
	('note'			, 'bright green'),
	('GET'			, 'bright green'),
	('info'			, 'bright cyan'),
	('debug'		, 'bright magenta'),
])