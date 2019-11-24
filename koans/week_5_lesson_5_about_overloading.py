#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutClassMethods in the Ruby Koans
#

from runner.koan import *

class AboutOverloading(Koan):
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

        def bark(self):
            return "woof woof"

    #1      
    def test_subclasses_can_overload_existing_behavior(self):
        chico = self.Chihuahua("Chico")
        self.assertEqual(__, chico.bark())

        fido = self.Dog("Fido")
        self.assertEqual(__, fido.bark())

    # ------------------------------------------------------------------

    class BullDog(Dog):
        def bark(self):
            return super().bark() + ", GRR"
    #2
    def test_subclasses_can_invoke_parent_behavior_via_super(self):
        ralph = self.BullDog("Ralph")
        self.assertEqual(__, ralph.bark())

    # ------------------------------------------------------------------

    class GreatDane(Dog):
        def growl(self):
            return super().bark() + ", GROWL"
    
    #3
    def test_super_works_across_methods(self):
        george = self.GreatDane("George")
        self.assertEqual(__, george.growl())

    # ---------------------------------------------------------

    class Pug(Dog):
        def __init__(self, name):
            pass

    class Greyhound(Dog):
        def __init__(self, name):
            super().__init__(name)
    
    #4
    def test_base_init_does_not_get_called_automatically(self):
        snoopy = self.Pug("Snoopy")
        with self.assertRaises(___): name = snoopy.name

    #5
    def test_base_init_has_to_be_called_explicitly(self):
        boxer = self.Greyhound("Boxer")
        self.assertEqual(__, boxer.name)