======================
Prism — colourful logs
======================

A command line log colouriser utility.


Installation
------------

    (sudo) pip install logprism


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
