# Prism -- colourful logs

A command line log colouriser utility. See 'prism -h' for help.
Tested with Python 2.6, Python 2.7 and Python 3.2.


## Installation


Make a symlink to prism.py, and ensure it's in your path. For example:

    # replace ~/code below with the dir you want to install to -- this shell variable is not needed for running
    export PRISM_CODE=~/code
    mkdir $PRISM_CODE
    cd $PRISM_CODE

    git clone git@github.com:peterhil/prism.git

    mkdir ~/bin
    cd ~/bin
    ln -s "$PRISM_CODE/prism/prism.py" prism


### To add ~/bin to your path:

    mkdir ~/bin
    cd ~/bin

    # If using ZSH:
    $EDITOR ~/.zshrc

    # Add following two lines to ~/.zshrc
    typeset -U path
    path=(~/bin $path)

    # Using BASH:
    $EDITOR ~/.bashrc

    # Add following line towards the end
    export PATH="~/bin:$PATH"


## Optional dependencies

    pip install watchdog


## Usage examples

    prism -g /var/log/*.log
    prism -m /var/log/apache2/*log
    prism /opt/local/var/macports/logs/*/*.log


## TODO

- Make a line cache (count total lines with `wc -l`) from the end of the file using some blocksize.
  a) Can be done with readlines() first. Then seek and read blocksize bytes from len(file)-blocksize and update cache.
  b) Later enable ncurses scrolling for earlier lines?
  c) Show n lines by default (a screenful / filecount?)

- isatty returns true only when io is from stdin or stdout!
  It's false when piping! Otherwise when not piping, it's true eg. when input is from command line by user!
  See: http://blog.yjl.im/2010/04/handling-standard-input-in-python.html
