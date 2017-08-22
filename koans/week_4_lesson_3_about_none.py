#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutNil in the Ruby Koans
#

from runner.koan import *

class AboutNone(Koan):

    #1
    def test_none_is_an_object(self):
        self.assertEqual(__, type(None))

    #2
    def test_none_is_universal(self):
        "There is only one None"
        self.assertEqual(____, None is None)

    #3
    def test_none_is_distinct(self):
        """
        None is distinct from other things which are False.
        """
        self.assertEqual(__, None is not 0)
        self.assertEqual(__, None is not False)
