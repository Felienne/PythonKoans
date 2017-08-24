#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutExceptions(Koan):

    #1
    def test_catch_problems(self):

        try:
            result = 12 / 0
        except Exception:
            result = "You can't divide by zero, silly."

        self.assertEqual(__, result)

    #2
    def test_can_return_message(self):

        try:
            result = 12 / 0
        except Exception as ex:
            result = ex.args[0]

        self.assertEqual(__, result)

    #3
    def test_types_of_exceptions(self):

        try:
            the_file = open("spoon.txt")
        except ZeroDivisionError as ex:
            result = "You found a division error!"

        except IOError as ex:
            result = "There is no spoon"

        self.assertEqual(__, result)

    #4
    def test_finally(self):

        try:
            result = 12 / 0
        except ZeroDivisionError:
            result = "You can't divide by zero, silly."
        finally:
            result = "Nevermind"

        self.assertEqual(__, result)

    #5
    def test_finally_success(self):

        try:
            result = 12 / 3
        except ZeroDivisionError:
            result = "You can't divide by zero, silly."
        finally:
            result = "Nevermind"

        self.assertEqual(__, result)

    #6  TODO nog niet in Stepik
    def test_else_clause(self):
        result = None
        try:
            result = 12 / 3
        except ZeroDivisionError:
            result = "You can't divide by zero, silly."
        else:
            to_print = result

        self.assertEqual(__, to_print)


    #7
    def test_assert_is_raised(self):
        with self.assertRaises(__):
            result = 12 / 0




