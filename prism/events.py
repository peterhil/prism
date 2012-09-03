#!/usr/bin/env python
# encoding: utf-8; tab-width: 4
#
# Copyright (c) 2012, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under 3-clause BSD license.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

import config
import fileinput
import os
import sys

from output import log, outputlines
from watchdog.events import FileSystemEventHandler


class PrismEventHandler(FileSystemEventHandler):
    """Prints all lines from modified files."""

    def __init__(self, files):
        self._files = files
        super(PrismEventHandler, self).__init__()

    def output(self, event):
        what = 'directory' if event.is_directory else 'file'
        log.debug("Got %s event at path '%s'" % (what, event.src_path))

        if what == 'file':
            if event.src_path in self._files or os.path.dirname(event.src_path) in self._files:
                print("\n==> %s <==" % os.path.basename(event.src_path))
                outputlines(fileinput.input(event.src_path), grep=config.grep_opt, match_only=config.match_opt)
            else:
                log.debug("Skipping not watched file: %s" % event.src_path)

    def on_moved(self, event):
        super(PrismEventHandler, self).on_moved(event)

        # TODO handle renames
        what = 'directory' if event.is_directory else 'file'
        log.info("Moved %s: from %s to %s", what, event.src_path, event.dest_path)

    def on_created(self, event):
        super(PrismEventHandler, self).on_created(event)
        self.output(event)

    def on_deleted(self, event):
        super(PrismEventHandler, self).on_deleted(event)

        # TODO handle deletions
        what = 'directory' if event.is_directory else 'file'
        log.info("Deleted %s: %s", what, event.src_path)

    def on_modified(self, event):
        super(PrismEventHandler, self).on_modified(event)
        self.output(event)
