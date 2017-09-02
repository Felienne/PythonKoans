#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

from . import jims_animals
from . import joes_animals

counter = 0 # Global

class AboutScope(Koan):


    #1
    def test_variable_with_same_name_is_different_variable(self):
        counter = 12
        self.assertEqual(__, counter)

    #2
    def test_global_access_is_possible_with_keyword(self):
        global counter
        self.assertEqual(__, counter)

    # let op! Kijk even of we dit in Stepik krijgen!
    # je kunt met fileIO een file schrijven (weet ik zeker)
    # en dan importen (denk ik)
    # zo niet, dan mail even dan droppen we de relevante koans

    #3
    def test_dog_is_not_available_in_the_current_scope(self):
        with self.assertRaises(___): fido = Dog()

    #4
    def test_you_can_reference_nested_classes_using_the_scope_operator(self):
        fido = jims_animals.Dog()
        # name 'jims' module name is taken from jims_animals.py filename

        rover = joes_animals.Dog()
        self.assertEqual(__, fido.identify())
        self.assertEqual(__, rover.identify())

        self.assertEqual(__, type(fido) == type(rover))
        self.assertEqual(__, jims_animals.Dog == joes_animals.Dog)

    # ------------------------------------------------------------------

    class str:
        """Fake string. So sad!"""

    #5
    def test_nested_string_is_not_the_same_as_the_system_string(self):
        self.assertEqual(__, self.str.__doc__)

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

    def inside_local(self):
        msg = "Outside!"

        def inside():
            msg = "Inside!"
            print(msg)

        inside()
        print(msg)


    def inside_non_local(self):
        msg = "Outside!"

        def inside():
            nonlocal msg
            msg = "Inside!"
            print(msg)

        inside()
        print(msg)


    #9
    def test_getting_something_locally(self):
        self.assertEqual(__, self.inside_local())

    #10
    def test_getting_something_nonlocally(self):
        self.assertEqual(__, self.inside_non_local())

    # ------------------------------------------------------------------

    global deadly_bingo
    deadly_bingo = [4, 8, 15, 16, 23, 42]

    #11
    def test_global_attributes_can_be_created_in_the_middle_of_a_class(self):
        self.assertEqual(__, deadly_bingo[5])
