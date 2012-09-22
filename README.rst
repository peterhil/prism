======================
Prism — colourful logs
======================

A command line log colouriser utility. See 'prism -h' for help and usage.
Tested with Python 2.6, Python 2.7 and Python 3.2.


Installation
------------

    (sudo) pip install logprism


Dependencies
------------

- argh (argument parsing)
- ordereddict (if using Python 2.6)
- pytest (for testing)
- watchdog (for watching log files with -w option)


Usage examples
--------------

    prism -g /var/log/\*.log

    prism -m /var/log/apache2/\*log

    prism /opt/local/var/macports/logs/\*\/\*.log


Todo
----

- Show some tail lines when using -w: Make a line cache (count total lines with `wc -l`) from the end of the file using some blocksize.

  a) Can be done with readlines() first. Then seek and read blocksize bytes from len(file)-blocksize and update cache.
  b) Later enable ncurses scrolling for earlier lines?
  c) Show n lines by default (a screenful / filecount?)
