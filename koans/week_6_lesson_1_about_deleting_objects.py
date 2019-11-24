#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutDeletingObjects(Koan):
    #1
    def test_del_can_remove_from_list(self):
        lottery_nums = [4, 8, 15, 16, 23, 42]
        del lottery_nums[1]
        del lottery_nums[2:4]

        self.assertEqual(___, lottery_nums)

    #2
    def test_del_can_remove_entire_lists(self):
        lottery_nums = [4, 8, 15, 16, 23, 42]
        del lottery_nums

        with self.assertRaises(___): win = lottery_nums

    # ====================================================================

    class Bird:
        def __init__(self):
            self.wings = 2

        def fly(self):
            return "I believe I can fly"


    #3
    def test_del_can_remove_attributes_from_instances(self):
        flappy = self.Bird()
        del flappy.wings

        try:
            number_of_wings = flappy.wings
        except AttributeError as e:
            error_message = e.args[0]

        self.assertEqual(error_message, __)

        polly = self.Bird()
        number_of_wings = polly.wings

        self.assertEqual(number_of_wings, __)

    #4
    def test_del_can_remove_methods(self):
        flappy = self.Bird()
        polly = self.Bird()

        del self.Bird.fly

        try:
            still_available = flappy.fly()
        except AttributeError as e:
            error_message_flappy = e.args[0]
        self.assertEqual(error_message_flappy, __)

        try:
            still_available = polly.fly()
        except AttributeError as e:
            error_message_polly = e.args[0]
        self.assertEqual(error_message_polly, __)

