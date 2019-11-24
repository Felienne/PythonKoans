#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutClassMethods in the Ruby Koans
#

from runner.koan import *

class AboutClassAttributes(Koan):
    class Dog:
        """I am a dog without a name."""
        bionomal_name = "Canine"

    #1
    def test_classes_have_their_own_attributes_too(self):
        fido = self.Dog()
        self.assertEqual(__, fido.bionomal_name)

    #2
    def test_attributes_are_per_instance(self):
        fido = self.Dog()   
        fluffy = self.Dog()
        self.assertEqual(_____, fido.bionomal_name == fluffy.bionomal_name)
        fido.bionomal_name = "Dogum"
        self.assertEqual(______, fido.bionomal_name == fluffy.bionomal_name)

    #3
    def test_defining_attributes_on_individual_objects(self):
        fido = self.Dog()
        fido.legs = 4

        self.assertEqual(__, fido.legs)

    #4
    def test_attributes_are_not_shared(self):
        fido = self.Dog()
        fido.legs = 4
        fluffy = self.Dog()

        with self.assertRaises(___): fluffy.legs


    #5
    def test_defining_functions_on_individual_objects(self):
        fido = self.Dog()
        fido.bark = lambda x : 'bark ' + x

        self.assertEqual(__, fido.bark("I like swimming"))

    #6
    def test_other_objects_are_not_affected_by_these_singleton_functions(self):
        fido = self.Dog()
        fido.bark = lambda x : 'bark ' + x

        self.assertEqual(__, fido.bark("I like swimming"))

        rover = self.Dog()

        with self.assertRaises(___): rover.wag()


