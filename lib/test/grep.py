#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2012, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under 3-clause BSD license.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

from unittest import TestCase
from ..grep import *


class GrepTest(TestCase):

    def match_test(self):
    	lines = [
    		"[Sun Apr 08 12:51:52 2012] [notice] Digest: done",
    		"[Mon Jul 11 09:26:13 2011] [error] [client ::1] File does not exist: /Library/WebServer/Documents/favicon.ico",
    	]

    	for line in lines:
    		match = re.search(pattern, line)
    		self.assertTrue(
    			match,
    			"Regexp pattern '{0}' didn't match line '{1}'".format(pattern, line)
    		)