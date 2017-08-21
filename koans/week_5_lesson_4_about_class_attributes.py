#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutClassMethods in the Ruby Koans
#

from runner.koan import *

class AboutClassAttributes(Koan):
    class Dog:
        "I am a dog without a name."
        latin_name = "Canine"

    def test_classes_have_their_own_attributes_too(self):
        fido = self.Dog()
        self.assertEqual(__, fido.latin_name)


    def test_attrubutes_are_shared_by_instances(self):
        fido = self.Dog()
        fluffy = self.Dog()
        self.assertEqual(__, fido.latin_name == fluffy.latin_name)


    def test_defining_attributes_on_individual_objects(self):
        fido = self.Dog()
        fido.legs = 4

        self.assertEqual(__, fido.legs)

    def test_attributes_are_not_shared(self):
        fido = self.Dog()
        fido.legs = 4
        fluffy = self.Dog()

        with self.assertRaises(___): fluffy.legs


    def test_defining_functions_on_individual_objects(self):
        fido = self.Dog()
        fido.bark = lambda x : 'bark ' + x

        self.assertEqual(__, fido.bark("I like swimming"))

    def test_other_objects_are_not_affected_by_these_singleton_functions(self):
        fido = self.Dog()
        fido.bark = lambda x : 'bark ' + x

        self.assertEqual(__, fido.bark("I like swimming"))

        rover = self.Dog()

        with self.assertRaises(___): rover.wag()


