#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutInheritance(Koan):
    class Dog:
        def __init__(self, name):
            self._name = name

        @property
        def name(self):
            return self._name

        def bark(self):
            return "WOOF"

    class Chihuahua(Dog):
        def wag(self):
            return "happy"

    #1
    def test_dogs_are_still_dogs(self):
        boef = self.Dog('Boef')
        self.assertEqual(self.Dog, __)

    #2
    def test_but_what_are_chihuahuas(self):
        tinkerbell = self.Chihuahua('Tinkerbell')
        self.assertEqual(__, type(tinkerbell))

    #3
    def test_subclasses_have_the_parent_as_an_ancestor(self):
        self.assertEqual(__, issubclass(self.Chihuahua, self.Dog))

    #4
    def test_all_defined_classes_ultimately_inherit_from_object_class(self):
        self.assertEqual(__, issubclass(self.Chihuahua, object))

    #5
    def test_all_built_in_classes_ultimately_inherit_from_object_class(self):
        self.assertEqual(__, issubclass(str, object))

    #6
    def test_instances_inherit_behavior_from_parent_class(self):
        chico = self.Chihuahua("Chico")
        self.assertEqual(__, chico.name)

    #7
    def test_subclasses_add_new_behavior(self):
        chico = self.Chihuahua("Chico")
        self.assertEqual(__, chico.wag())

        fido = self.Dog("Fido")
        with self.assertRaises(___): fido.wag()


