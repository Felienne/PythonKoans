#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import re

# Starting a classname or attribute with an underscore normally implies Private scope.
# However, we are making an exception for __ and ___.

__all__ = [ "__", "___", "____", "_____","______","_______", "_________", "Koan" ]

__ = "-=> FILL ME IN! <=-"
______ = "-=> FILL ME IN! <=-"
_______ = "-=> FILL ME IN! <=-"

class ___(Exception):
    pass

____ = "-=> TRUE OR FALSE? <=-"

_____ = 0

def _________(parameter1):
    return "please choose the right method"


class Koan(unittest.TestCase):
    pass
