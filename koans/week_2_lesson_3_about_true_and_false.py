#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutTrueAndFalse(Koan):
    # 1
    def test_true_is_true(self):
        bear_poop_place = ""

        if True:
            bear_poop_place = ""

        self.assertEqual("woods", bear_poop_place)

    # 2
    def test_false_is_false(self):
        dessert = "chocolate"

        if False:
            dessert = "ketchup"

        self.assertEquals(__, dessert);

    # 3
    def test_false_number_is_false(self):
        dessert = "chocolate"

        if 0:
            dessert = "ketchup"

        self.assertEquals(__, dessert);


    # 4
    def test_empty_string_is_false(self):
        dessert = "chocolate"

        if "":
            dessert = "ketchup"

        self.assertEquals(__, dessert);

    # 5
    def test_empty_set_is_false(self):
        dessert = "chocolate"

        if {}:
            dessert = "ketchup"

        self.assertEquals(__, dessert);

    # 6
    def test_empty_list_is_false(self):
        dessert = "chocolate"

        if []:
            dessert = "ketchup"

        self.assertEquals(__, dessert);

    # 7
    def test_everything_else_is_treated_as_true(self):
        dessert = "chocolate"

        if 2:
            dessert = "ketchup"

        self.assertEquals(__, dessert);


