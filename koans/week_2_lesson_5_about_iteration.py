#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutIteration(Koan):

    #2
    def test_for_statement(self):
        one_to_10 = range(10)
        ten_little_squares = []

        for i in one_to_10:
            ten_little_squares.append(i*i)

        self.assertEqual(__, ten_little_squares)

    #TODO: hier nog een keer continue en break

    #3
    def test_for_statement_over_list(self):
        one_direction = ["harry", "niall", "louis", "liam", "zayn"]
        one_direction_print = []

        for member in one_direction:
            one_direction_print.append(member.capitalize())
        self.assertEqual([__, __, __, __, __], one_direction_print)


    #4
    def test_iterating_with_next(self):
        stages = iter(['alpha', 'beta', 'gamma'])

        self.assertEqual(__, next(stages))
        next(stages)

        self.assertEqual(__, next(stages))
        next(stages)

        self.assertEqual(__, next(stages))
        next(stages)

