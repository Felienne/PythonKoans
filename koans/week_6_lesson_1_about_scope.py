#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

from . import jims_animals
from . import joes_animals

counter = 0 # Global

# let op! Kijk even of we dit in Stepik krijgen!
# je kunt met fileIO een file schrijven (weet ik zeker)
# en dan importen (denk ik)
# zo niet, dan mail even dan droppen we de relevante koans

class AboutScope(Koan):


    #1
    def test_dog_is_not_available_in_the_current_scope(self):
        with self.assertRaises(___): fido = Dog()

    #2
    def test_you_can_reference_nested_classes_using_the_scope_operator(self):
        fido = jims_animals.Dog()
        # name 'jims' module name is taken from jims_animals.py filename

        rover = joes_animals.Dog()
        self.assertEqual(__, fido.identify())
        self.assertEqual(__, rover.identify())

        self.assertEqual(__, type(fido) == type(rover))
        self.assertEqual(__, jims_animals.Dog == joes_animals.Dog)

    # ------------------------------------------------------------------

    #3
    class str:
        pass

    #4
    def test_bare_bones_class_names_do_not_assume_the_current_scope(self):
        self.assertEqual(__, AboutScope.str == str)

    #5
    def test_nested_string_is_not_the_same_as_the_system_string(self):
        self.assertEqual(__, self.str == type("HI"))

    #6
    def test_str_without_self_prefix_stays_in_the_global_scope(self):
        self.assertEqual(__, str == type("HI"))

    # ------------------------------------------------------------------

    PI = 3.1416

    #7
    def test_constants_are_defined_with_an_initial_uppercase_letter(self):
        self.assertAlmostEqual(_____, self.PI)
        # Note, floating point numbers in python are not precise.
        # assertAlmostEqual will check that it is 'close enough'

    #8
    def test_constants_are_assumed_by_convention_only(self):
        self.PI = "rhubarb"
        self.assertEqual(_____, self.PI)
        # There aren't any real constants in python. Its up to the developer
        # to keep to the convention and not modify them.

    # ------------------------------------------------------------------

    def increment_using_local_counter(self, counter):
        counter = counter + 1

    def increment_using_global_counter(self):
        global counter
        counter = counter + 1

    #9
    def test_incrementing_with_local_counter(self):
        global counter
        start = counter
        self.increment_using_local_counter(start)
        self.assertEqual(__, counter == start + 1)

    #10
    def test_incrementing_with_global_counter(self):
        global counter
        start = counter
        self.increment_using_global_counter()
        self.assertEqual(__, counter == start + 1)

    # ------------------------------------------------------------------

    def local_access(self):
        stuff = 'eels'
        def from_the_league():
            stuff = 'this is a local shop for local people'
            return stuff
        return from_the_league()

    def nonlocal_access(self):
        stuff = 'eels'
        def from_the_boosh():
            nonlocal stuff
            return stuff
        return from_the_boosh()

    #11
    def test_getting_something_locally(self):
        self.assertEqual(__, self.local_access())

    #12
    def test_getting_something_nonlocally(self):
        self.assertEqual(__, self.nonlocal_access())

    # ------------------------------------------------------------------

    global deadly_bingo
    deadly_bingo = [4, 8, 15, 16, 23, 42]

    #13
    def test_global_attributes_can_be_created_in_the_middle_of_a_class(self):
        self.assertEqual(__, deadly_bingo[5])
