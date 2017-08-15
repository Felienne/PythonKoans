#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutSets(Koan):
    #2
    def test_sets_have_no_duplicates(self):
        highlanders = ['MacLeod', 'MacLeod', 'Matunas', 'Matunas', 'Matunas', 'Malcolm', 'Malcolm']

        there_can_only_be_only_one = set(highlanders)

        self.assertEqual(__, there_can_only_be_only_one)
    #3
    def test_empty_sets_have_different_syntax_to_populated_sets(self):
        self.assertEqual(__, {1, 2, 3})
        self.assertEqual(__, set())

    #4
    def test_dictionaries_and_sets_use_same_curly_braces(self):
        self.assertEqual(__, type({1, 2, 3}))
        self.assertEqual(__, type({'one': 1, 'two': 2}))
        self.assertEqual(__, type({}))

    #5
    def test_creating_sets_using_strings(self):
        self.assertEqual(__, {'12345'})
        self.assertEqual(__, set('12345'))

    #6
    def test_convert_the_set_into_a_list_to_sort_it(self):
        self.assertEqual(__, sorted(set('52314')))


    #7
    def test_set_have_arithmetic_operators(self):
        beatles = {'John', 'Ringo', 'George', 'Paul'}
        dead_musicians = {'John', 'George', 'Elvis', 'Tupac', 'Bowie'}

        great_musicians = beatles | dead_musicians
        self.assertEqual(__, great_musicians)

        living_beatles = beatles - dead_musicians
        self.assertEqual(__, living_beatles)

        dead_beatles = beatles & dead_musicians
        self.assertEqual(__, dead_beatles)

    #8
    def test_we_can_compare_subsets(self):

        beatles = {'John', 'Ringo', 'George', 'Paul'}
        dead_musicians = {'John', 'George', 'Elvis', 'Tupac', 'Bowie'}

        dead_beatles = beatles & dead_musicians

        self.assertEqual(__, dead_beatles <= beatles)
        self.assertEqual(__, dead_beatles.issubset(beatles) )

    #9
    def test_we_can_query_set_membership(self):
        beatles = {'John', 'Ringo', 'George', 'Paul'}
        one_direction = {"Harry", "Niall", "Louis", "Liam", "Zayn"}

        self.assertEqual(__, 'John' in beatles )
        self.assertEqual(__, 'Ringo' not in one_direction)