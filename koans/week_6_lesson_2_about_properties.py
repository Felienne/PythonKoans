#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Partially based on AboutMessagePassing in the Ruby Koans
#

from runner.koan import *

class AboutProperties(Koan):
    class Person:
        def __init__(self):
            self.age = 10

        def drive(self):
            if self.age < 18:
                return  "Too young"
            else:
                return "VROOM VROOM"

    #1
    def test_fields_are_mutable(self):
        the_flash = self.Person()
        self.assertEqual("Too young", the_flash.drive())
        the_flash.__ = 24
        self.assertEqual("VROOM VROOM", the_flash.drive())

    class ImmutablePerson:
        def __init__(self):
            self._age = 10

        @property
        def age(self):
            return self._age

    #2
    def test_properties_can_be_read_only(self):
        the_flash = self.ImmutablePerson()
        self.assertEqual(10, the_flash.age)

        with self.assertRaises(___):
            the_flash.age = 24

    class MutablePerson:
        def __init__(self):
            self._age = 10

        @property
        def age(self):
            return self._age

        @age.setter
        def age(self, value):
            self._age = value

    #3
    def test_adding_setters_makes_properties_mutable(self):
        the_flash = self.MutablePerson()
        self.assertEqual(_____, the_flash.age)
        the_flash.age = 24
        self.assertEqual(______, the_flash.age)

    #4
    def test_properties_are_methods_that_can_be_accessed_like_variables(self):
        the_flash = self.MutablePerson()
        self.assertEqual(10, the_flash.age)
        the_flash.age += _____
        self.assertEqual(24, the_flash.age)

    class Doctor:
        def __init__(self):
            self._age = 903

        @property
        def age(self):
            return self._age

        @age.setter
        def age(self, value):
            if value < self.age:
                pass
                # nice try! you can't get any younger
            else:
                self._age = value

    #5
    def test_validation3(self):
        jodie = self.Doctor()
        self.assertEqual(903, jodie.age)
        jodie.age += 9
        self.assertEqual(__, jodie.age)

    #6
    def test_validation(self):
        david = self.Doctor()
        self.assertEqual(903, david.age)
        david.age = 9
        self.assertEqual(__, david.age)

    #7
    def test_validation2(self):
        william = self.Doctor()
        self.assertEqual(903, william.age)
        william.age -= 9
        self.assertEqual(__, william.age)

    class TicTacToe:
        def __init__(self):
            self._x = 0
            self._y = 0

        @property
        def x(self):
            return self._x

        @property
        def y(self):
            return self._y

        @x.setter
        def x(self, value):
            __

        @y.setter
        def y(self, value):
            __

    #8
    def test_assigning_values(self):
        game = self.TicTacToe()
        game.x = 3
        self.assertEqual(__,game.x)
        # hint: you need to write the setter

    #9
    def test_highest_value_allowed_is_three(self):
        game = self.TicTacToe()
        game.y = 2
        self.assertEqual(2,game.y)
        game.y = 4
        self.assertEqual(3,game.y)
        # hint: you need to write the setter

    #10
    def test_lowest_value_allowed_is_one(self):
        game = self.TicTacToe()
        game.y = 2
        self.assertEqual(2,game.y)
        game.y = 0
        self.assertEqual(1,game.y)
        # hint: you need to adapt the setter

    class Cat:
        @property
        def name(self):
            return self._name

        @name.setter
        def name(self,value):
            if value.lower() == "cat":
                raise ValueError("cats deserve a proper name")
            elif value.lower() == "dog":
                raise TypeError("what is wrong with you?!")
            else:
                self._name = value

    #11
    def test_validation_reject_invalid_values(self):
        bob = self.Cat()
        with self.assertRaises(ValueError):
            bob.name = __

        bob = self.Cat()
        with self.assertRaises(___):
            bob.name = "dog"

    class Counter:
        def __init__(self):
            self._count = 0

        @property
        def count(self):
            self._count += _____
            return self._count

    #12
    def test_properties_allow_calculation(self):
        graaf_tel = self.Counter()
        self.assertEqual(1, graaf_tel.count)
        self.assertEqual(2, graaf_tel.count)
        self.assertEqual(3, graaf_tel.count)

    class Dada:
        def __init__(self):
            self._names_are_meaningless = "Oote oote oote"

        @property
        def poetry(self):
            return self._names_are_meaningless


        @poetry.setter
        def poetry(self,value):
            self._names_are_meaningless = value

    #13
    def test_matching_properties_and_fields_are_used_by_convention_only(self):
        dada = self.Dada()
        self.assertEqual(__, dada.poetry)
        dada.__ = "Boe"
        self.assertEqual("Boe", dada.poetry)
        self.assertEqual(__, dada.names_are_meaningless)





