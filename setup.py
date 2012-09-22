#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2012, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under 3-clause BSD license.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

import sys
from distutils.core import setup

PACKAGE_NAME = 'Prism'
PACKAGE_VERSION = '0.1.0'
PACKAGES = ['prism']

setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    packages=PACKAGES,
    requires = [
        'argh (>=0.15.0)',
        'watchdog (>=0.6.0)',
        'ordereddict (>=1.1)' if sys.version <= (2, 7, 0) else 'collections',
        'pytest (>=2.2.0)',
    ],
    scripts=['bin/prism'],

    description="#{PACKAGE_NAME} – colourise log levels and other keys on log files (with ANSI characters codes)",
    author='Peter Hillerström',
    author_email='peter.hillerstrom@gmail.com',
    license='BSD License',
    url='https://github.com/peterhil/prism',

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Bug Tracking',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Internet :: Log Analysis',
        'Topic :: System :: Logging',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Systems Administration',
        'Topic :: Text Processing :: Filters',
        'Topic :: Utilities',
    ]
)