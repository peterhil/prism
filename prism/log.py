#!/usr/bin/env python -u
# encoding: utf-8
#
# Copyright (c) 2012, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under 3-clause BSD license.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

import logging
import sys

log = logging.getLogger('Prism')
log.addHandler(logging.StreamHandler(sys.stderr))
log.setLevel(logging.INFO)
