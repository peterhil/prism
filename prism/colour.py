#!/usr/bin/env python -u
#
# Copyright (c) 2012, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under 3-clause BSD license.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

"""This module generates ANSI colour and character codes for terminals.
See: http://en.wikipedia.org/wiki/ANSI_escape_code#CSI_codes"""

__all__ = ["code", "colourcode", "colour"]

import math


CSI = "\x1b["

COLOUR = {
    "black": 0,
    "red": 1,
    "green": 2,
    "yellow": 3,
    "blue": 4,
    "magenta": 5,
    "cyan": 6,
    "white": 7,
    "k": 0,
    "r": 1,
    "g": 2,
    "y": 3,
    "b": 4,
    "m": 5,
    "c": 6,
    "w": 7,
}

# Offsets
FORE = 30
BACK = 40
BRIGHT = 60


def code(code, op="m"):
    if code == 0 or code != "":
        return CSI + str(code) + op
    else:
        return ""


def colourcode(name, back=False):
    """
    Return ANSI colour code for a colour name.
    If 'back' is True, returns a background colour.
    """
    if not name:
        return ""

    parts = str(name).lower().split()
    bright = BRIGHT * int("bright" in parts)

    try:
        colourname = next(filter(lambda s: s in COLOUR, parts), None)
    except StopIteration:
        pass

    if isinstance(COLOUR.get(colourname), int):
        colour = COLOUR.get(colourname) + (BACK if back else FORE)
        code = bright + colour
    else:
        code = ""

    return code


def colour(fore="", back=""):
    colours = [str(colourcode(fore)), str(colourcode(back, True))]

    return code(";".join(filter(None, colours)))


def logo(text, colours="rygcb", repeat=True):
    res = ""
    if repeat:
        # Repeat colours string to make it at least as long as text
        colours *= int(math.ceil(len(text) / len(colours)))
    for c, letter in zip(colours, text):
        res += "{} {} ".format(colour(c, "bright " + c), letter)

    return res + code(0)


def prism_logo(extra=""):
    return "\n {}\n  {} coloured logs {}  {}\n".format(
        logo("PRISM", "rygcb"), code(7), code(0), extra
    )
