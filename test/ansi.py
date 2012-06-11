#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2012, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under 3-clause BSD license.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

from unittest import TestCase
from ..ansi import *


class AnsiTest(TestCase):

    def colourcode_test(self):
    	test_data = [
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
    	]

    	for code, name in test_data:
	        self.assertEquals(code, colourcode(name))
        	self.assertEquals(code + 10 if isinstance(code, int) else '', colourcode(name, back=True))


    def colour_test(self):
    	self.assertEquals('\x1b[31;m', colour('RED'))