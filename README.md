# Prism -- colourful logs

A command line log colouriser utility
See 'prism -h' for help.


## Usage examples

    % prism -g /var/log/*.log
    % prism -m /var/log/apache2/*log
    % prism /opt/local/var/macports/logs/*/*.log


## TODO

- Make a line cache (count total lines with `wc -l`) from the end of the file using some blocksize.
  a) Can be done with readlines() first. Then seek and read blocksize bytes from len(file)-blocksize and update cache.
  b) Later enable ncurses scrolling for earlier lines?
  c) Show n lines by default (a screenful / filecount?)

- isatty returns true only when io is from stdin or stdout!
  It's false when piping! Otherwise when not piping, it's true eg. when input is from command line by user!
  See: http://blog.yjl.im/2010/04/handling-standard-input-in-python.html

