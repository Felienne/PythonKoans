#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutIteration(Koan):

    # 1
    def test_for_statement(self):
        one_to_10 = range(10)
        ten_little_squares = []

        for i in one_to_10:
            ten_little_squares.append(i*i)

        self.assertEqual(__, ten_little_squares)

    # 2
    def test_for_statement_with_break(self):
        one_to_10 = range(10)
        four_little_squares = []

        for i in one_to_10:
            if i == 4:
                break
            four_little_squares.append(i*i)

        self.assertEqual(__, four_little_squares)

    # 3
    def test_for_statement_with_continue(self):
        one_to_10 = range(10)
        I_hate_nine = []

        for i in one_to_10:
            if i == 3:
                continue
            I_hate_nine.append(i*i)

        self.assertEqual(__, I_hate_nine)


    # 4
    def test_for_statement_over_list(self):
        one_direction = ["harry", "niall", "louis", "liam", "zayn"]
        one_direction_print = []

        for member in one_direction:
            one_direction_print.append(member.capitalize())
        self.assertEqual([__, __, __, __, __], one_direction_print)


    # 5
    def test_iterating_with_next(self):
        stages = iter(['alpha', 'beta', 'gamma'])

        self.assertEqual(__, next(stages))
        next(stages)

        self.assertEqual(__, next(stages))
        next(stages)

        self.assertEqual(__, next(stages))
        next(stages)

