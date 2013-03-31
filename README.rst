Prism — colourful logs
======================

A command line log colouriser utility.


Installation
------------

From Python package index (Pypi_):

    (sudo) pip install logprism

or from Github_:

    (sudo) pip install watchdog  # optional

    git clone https://github.com/peterhil/prism.git

    cd prism

    (sudo) python setyp.py install


Dependencies
------------

All dependencies can be installed with pip_, usually by:

    pip install some-package

Required (automatically handled by pip):

- ordereddict (if using Python 2.6)

Optional (install manually with pip):

- watchdog (watch files and directories with the -w option. Recommended for Python 2.x only – doesn’t work with Python 3)

Developers only:

- pytest (test framework)
- tox (continuous integration)


Usage examples
--------------

Colourise stdin:

    tail -f /opt/local/var/log/couchdb/couch.log | prism


Grep some logs for messages with levels:

    prism -g /var/log/\*.log


Combine with grep command to find just specific levels:

    grep -iE '(warn|error)' /var/log/\*.log | prism -g


Match multiple log levels per line:

    prism -m /var/log/apache2/vhost\*log

    prism -m <(echo "Dribble me a debug or info lest I notice no create nor alter nor drop of your critical tables.")


Watch for a whole directory of logs for changes (and new files):

    prism -m -w /opt/local/var/log/nginx/


Some programs output normally to stderr, grab that output for prism:

    python run.py 2>&1 | prism



Test
----

Run unit tests:

    python setup.py test

Run continuous integration with tox (from an activated virtualenv, use tox -r to recreate CI envs):

    tox


Todo
----

- Show some tail lines when using -w: Make a line cache (count total lines with `wc -l`) from the end of the file using some blocksize.

  a) Can be done with readlines() first. Then seek and read blocksize bytes from len(file)-blocksize and update cache.
  b) Later enable ncurses scrolling for earlier lines?
  c) Show n lines by default (a screenful / filecount?)


.. _Github: https://github.com/peterhil/prism/
.. _Pypi: http://pypi.python.org/pypi/logprism
.. _pip: http://www.pip-installer.org/
