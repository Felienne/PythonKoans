#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutTrueAndFalse(Koan):
    # 1
    def true_is_true(self):
        if True:
            truth = 'true branch'
        else:
            truth = 'false branch'
        self.assertEqual(__, truth)

    # 2
    def zero_is_false(self):
        if 0:
            truth = 'true branch'
        else:
            truth = 'false branch'
        self.assertEqual(__, truth)

    # 3
    def empty_string_is_false(self):
        if "":
            truth = 'true branch'
        else:
            truth = 'false branch'
        self.assertEqual(__, truth)

    # 4
    def empty_set_is_false(self):
        if []:
            truth = 'true branch'
        else:
            truth = 'false branch'
        self.assertEqual(__, truth)

    # 5
    def empty_list_is_false(self):
        if []:
            truth = 'true branch'
        else:
            truth = 'false branch'
        self.assertEqual(__, truth)

    # 6
    def test_everything_else_is_treated_as_true(self):
        # try some crazy things!

        if 2:
            truth = 'true branch'
        else:
            truth = 'false branch'
        self.assertEqual(__, truth)


