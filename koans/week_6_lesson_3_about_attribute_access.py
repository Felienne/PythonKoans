#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Partially based on AboutMessagePassing in the Ruby Koans
#

from runner.koan import *

class AboutAttributeAccess(Koan):

    class TypicalObject:
        pass

    #1
    def test_calling_undefined_functions_normally_results_in_errors(self):
        typical = self.TypicalObject()

        with self.assertRaises(___): typical.foobar()

    #2
    def test_calling_getattribute_causes_an_attribute_error(self):
        typical = self.TypicalObject()

        with self.assertRaises(___): typical.__getattribute__('foobar')

        # THINK ABOUT IT:
        #
        # If the method __getattribute__() causes the AttributeError, then
        # what would happen if we redefine __getattribute__()?

    # ------------------------------------------------------------------

    class CatchAllAttributeReads:
        def __getattribute__(self, attr_name):
            return "Someone called '" + attr_name + "' and it could not be found"

    #3
    def test_all_attribute_reads_are_caught(self):
        catcher = self.CatchAllAttributeReads()

        self.assertEqual(catcher.foobar, __)

    #4
    def test_intercepting_return_values_can_disrupt_the_call_chain(self):
        catcher = self.CatchAllAttributeReads()

        self.assertEqual(catcher.foobaz, __) # This is fine

        try:
            catcher.foobaz(1)
        except TypeError as ex:
            err_msg = ex.args[0]

        self.assertRegex(err_msg, __)

    #5
    def test_changes_to_the_getattribute_implementation_affects_getattr_function(self):
        catcher = self.CatchAllAttributeReads()

        self.assertEqual(getattr(catcher, 'any_attribute'), __)

    # ------------------------------------------------------------------

    class WellBehavedFooCatcher:
        def __getattribute__(self, attr_name):
            if attr_name[:3] == "foo":
                return "Foo to you too"
            else:
                return super().__getattribute__(attr_name)

    #6
    def test_foo_attributes_are_caught(self):
        catcher = self.WellBehavedFooCatcher()

        self.assertEqual(__, catcher.foo_bar)
        self.assertEqual(__, catcher.foo_baz)

    #7
    def test_non_foo_messages_are_treated_normally(self):
        catcher = self.WellBehavedFooCatcher()

        with self.assertRaises(___): catcher.normal_undefined_attribute

    # ------------------------------------------------------------------

    class MinimalCatcher:
        class DuffObject: pass

        def __init__(self):
            self.no_of_getattr_calls = 0

        def __getattr__(self, attr_name):
            self.no_of_getattr_calls += 1
            return self.DuffObject

        def my_method(self):
            pass

    #8
    def test_getattr_ignores_known_attributes(self):
        catcher = self.MinimalCatcher()
        catcher.my_method()

        self.assertEqual(__, catcher.no_of_getattr_calls)

    #9
    def test_getattr_only_catches_unknown_attributes(self):
        catcher = self.MinimalCatcher()
        catcher.purple_flamingos()
        catcher.free_pie()

        self.assertEqual(__,
            type(catcher.give_me_duff_or_give_me_death()).__name__)

        self.assertEqual(__, catcher.no_of_getattr_calls)

    # ------------------------------------------------------------------

    class PossessiveSetter(object):
        def __setattr__(self, attr_name, value):
            new_attr_name =  attr_name

            if attr_name == 'comic':
                new_attr_name = "my_" + new_attr_name
            if attr_name == 'pie':
                new_attr_name = "a_" + new_attr_name

            object.__setattr__(self, new_attr_name, value)

    #10
    def test_setattr_intercepts_attribute_assignments(self):
        fanboy = self.PossessiveSetter()

        fanboy.pie = 'blueberry'

        self.assertEqual(__, fanboy.a_pie)
        self.assertEqual(__, fanboy.pie)

    # ------------------------------------------------------------------

    class ScarySetter:
        def __init__(self):
            self.num_of_coconuts = 9
            self._num_of_private_coconuts = 2

        def __setattr__(self, attr_name, value):
            new_attr_name =  attr_name

            if attr_name[0] != '_':
                new_attr_name = "altered_" + new_attr_name

            object.__setattr__(self, new_attr_name, value)

    #11
    def test_it_modifies_external_attribute_as_expected(self):
        setter = self.ScarySetter()
        setter.e = "mc hammer"

        self.assertEqual(__, setter.altered_e)

    #12
    def test_it_mangles_some_internal_attributes(self):
        setter = self.ScarySetter()

        try:
            coconuts = setter.num_of_coconuts
        except AttributeError:
            self.assertEqual(__, setter.altered_num_of_coconuts)

    #13
    def test_in_this_case_private_attributes_remain_unmangled(self):
        setter = self.ScarySetter()

        self.assertEqual(__, setter._num_of_private_coconuts)
