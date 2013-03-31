#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2012, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under 3-clause BSD license.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

from __future__ import with_statement

import sys
from distutils.core import setup, Command

from prism import VERSION

PACKAGE_NAME = 'logprism'
PACKAGE_VERSION = VERSION
PACKAGES = ['prism']

with open('README.rst', 'r') as readme:
    README_TEXT = readme.read()

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    packages=PACKAGES,
    requires = [
        'ordereddict (>=1.1)' if sys.version_info <= (2, 7, 0) else 'collections',
    ],
    scripts=['bin/prism'],

    description="Prism – Colourise log files (with ANSI characters codes)",
    long_description=README_TEXT,
    author='Peter Hillerström',
    author_email='peter.hillerstrom@gmail.com',
    license='BSD License',
    url='https://github.com/peterhil/prism',

    classifiers = [
        'Development Status :: 4 - Beta',
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
    ],
    cmdclass = {
        'test': PyTest
    },
)