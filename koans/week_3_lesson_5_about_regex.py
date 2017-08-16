#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
import re
class AboutRegex(Koan):
    """
        These koans are based on the Ben's book: Regular Expressions in 10 minutes.
        I found this books very useful so I decided to write a koans in order to practice everything I had learned from it.
        http://www.forta.com/books/0672325667/
    """

    def test_findall_multiple_times(self):
        being = "Malkovich, Malkovich Malkovich. Malkovich Malkovich Malkovich"
        m = re.findall('Malkovich', being)

        self.assertEqual(__, m)
        self.assertEqual(__, len(m))

    def test_matching_literal_text_not_case_sensitivity(self):
        movie_007 = "hello my name is bond, james bond. sadly my shift key is broken"

        self.assertEqual(re.findall("Bond", movie_007), __)
        self.assertEqual(re.findall("Bond", movie_007, re.IGNORECASE), __)


    def test_matching_numbers(self):
        address = "Beverly Hills 90210"
        numbers_only_regex = '[0-9]'

        numbers_only = re.findall(numbers_only_regex, address)
        self.assertEquals(__,numbers_only)

    def test_matching_numbers(self):
        address = "Beverly Hills 90210"
        lower_case_letters_only_regex = '[a-z]'

        lower_case_letters_only = re.findall(lower_case_letters_only_regex, address)
        self.assertEquals(__,lower_case_letters_only)

    def test_matching_set_character(self):
        boys_names = """
        Harry
        Perry
        Gary
        Lary
        Barry
        Terry
        """
        starts_with_b_or_h_then_arry = '[BH]arry'
        names_I_like = re.findall(starts_with_b_or_h_then_arry, boys_names)
        self.assertEquals(__,names_I_like)

    def test_matching_set_character(self):
        girls_names = """
        Evangeline
        Carolynn
        Mary
        Erica
        Eveline
        Sheryll
        """
        ends_with_ine = '[a-z]+ine'
        names_I_like = re.findall(ends_with_ine, girls_names,  re.IGNORECASE)
        self.assertEquals(__,names_I_like)


    def test_matching_anything_but(self):
        girls_names = """
        Evangeline
        Carolynn
        Mary
        Erica
        Eveline
        Sheryll
        """
        does_not_start_with_E = '[^E][a-z]+'
        names_I_like = re.findall(does_not_start_with_E, girls_names)
        self.assertEquals(__,names_I_like)


