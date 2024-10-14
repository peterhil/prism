[![image](https://img.shields.io/pypi/v/logprism.svg)](https://pypi.python.org/pypi/logprism)
[![image](https://img.shields.io/pypi/dm/logprism.svg)](https://pypi.python.org/pypi/logprism)
[![image](https://img.shields.io/pypi/l/logprism.svg)](https://pypi.python.org/pypi/logprism)

# Prism — colourful logs

A command line log colouriser utility.

## Installation

Install from PyPI using `pip`:

    pip install logprism

Install from source:

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

Colourise logs:

    prism /var/log/*.log

Grep logs for only messages with levels:

    prism -g /var/log/*.log

Match multiple log levels per line:

    prism -m /var/log/apache2/vhost\*log
    prism -m <(echo "Dribble me a debug or info lest I notice")

Watch for a whole directory of logs for changes (and new files):

    prism -m -w /opt/local/var/log/nginx/


### Pipe into Prism

Some programs output normally to stderr, grab that output for prism:

    python run.py 2>&1 | prism -m

Colourise tail output:

    tail -f /var/log/*.log | prism

Combine with grep command to find just specific levels:

    grep -iE '(warn|error)' /var/log/*.log | prism


## Test

Run unit tests:

    pytest

Run continuous integration with tox (from an activated virtualenv, use
tox -r to recreate CI envs):

    tox
