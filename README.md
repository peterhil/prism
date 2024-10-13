[![image](https://img.shields.io/pypi/v/logprism.svg)](https://pypi.python.org/pypi/logprism)
[![image](https://img.shields.io/pypi/dm/logprism.svg)](https://pypi.python.org/pypi/logprism)
[![image](https://img.shields.io/pypi/l/logprism.svg)](https://pypi.python.org/pypi/logprism)

# Prism — colourful logs

A command line log colouriser utility.

## Installation

From Python package index:

    pip install logprism

or from Github:

    git clone https://github.com/peterhil/prism.git
    cd prism
    pip install .

Development installation:

    git clone https://github.com/peterhil/prism.git
    cd prism
    python3.10 -m venv --prompt prism310 venv/py310
    source ./venv/py310/bin/activate
    pip install --editable .

## Usage examples

Colourise stdin:

    tail -f /var/log/system.log | prism

Grep some logs for messages with levels:

    prism -g /var/log/*.log

Combine with grep command to find just specific levels:

    grep -iE '(warn|error)' /var/log/*.log | prism -g

Match multiple log levels per line:

    prism -m /var/log/apache2/vhost\*log
    prism -m <(echo "Dribble me a debug or info lest I notice")

Watch for a whole directory of logs for changes (and new files):

    prism -m -w /opt/local/var/log/nginx/

Some programs output normally to stderr, grab that output for prism:

    python run.py 2>&1 | prism

## Test

Run unit tests:

    pytest

Run continuous integration with tox (from an activated virtualenv, use
tox -r to recreate CI envs):

    tox

## Todo

### Show some tail lines when using -w:

Make a line cache (count total
lines with `wc -l`) from the end of the file using some blocksize.

* a)	Can be done with readlines() first. Then seek and read blocksize
	bytes from len(file)-blocksize and update cache.
* b)  Later enable ncurses scrolling for earlier lines?
* c)  Show n lines by default (a screenful / filecount?)
