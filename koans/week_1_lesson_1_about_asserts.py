#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutAsserts(Koan):

    #2
    def test_assert_truth(self):
        # We shall contemplate truth by testing reality, via asserts.

        self.assertTrue(False) # This should be True

    #3
    def test_assert_with_message(self):
        # Enlightenment may be more easily achieved with appropriate messages.

        self.assertTrue(False, "This should be True -- Please fix this")

    #4
    def test_fill_in_values(self):
        # Sometimes we will ask you to fill in the values

        self.assertEqual(__, 1 + 1)

    #5
    def test_assert_equality(self):
        # To understand reality, we must compare our expectations against reality.

        expected_value = __
        actual_value = 1 + 1
        self.assertTrue(expected_value == actual_value)

    #6
    def test_a_better_way_of_asserting_equality(self):
        # Some ways of asserting equality are better than others.

        expected_value = __
        actual_value = 1 + 1

        self.assertEqual(expected_value, actual_value)



