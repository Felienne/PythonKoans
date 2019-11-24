#!/usr/bin/env python
# -*- coding: utf-8 -*-

#examples based on: https://www.thecodeship.com/patterns/guide-to-python-function-decorators/

from runner.koan import *


def greet(name):
    return "Hello there {0}!".format(name)

def bold_decorate(func):
    def func_wrapper(name):
        return "<b>{0}</b>".format(func(name))
    return func_wrapper

def italic_decorate(func):
    def func_wrapper(name):
        return "<i>{0}</i>".format(func(name))
    return func_wrapper

@bold_decorate
def bold_greet(name):
    return "Hello there {0}!".format(name)

@bold_decorate
@italic_decorate
def bold_and_italic_greet(name):
    return "Hello there {0}!".format(name)

def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("h1")
def header_greet(name):
    return "Hello there {0}!".format(name)

class AboutDecorators(Koan):

    #1
    def test_simple_greeting(self):
        self.assertEqual("Hello there Mary Lou!", _________(__))

    #2
    def test_decorating_a_function(self):
        get_bold = bold_decorate(greet)
        self.assertEqual(__, get_bold("Mary Lou"))
        self.assertEqual(__, bold_decorate(_________)("Peggy Sue"))

    #3
    def test_decorating_with_at(self):
        self.assertEqual(__, bold_greet("Richard Wayne Gary Wayne"))

    #4
    def test_stacking_decorators_normally(self):
        get_bold_and_italic = bold_decorate(italic_decorate(greet))
        self.assertEqual(__, get_bold_and_italic("Richard Wayne Gary Wayne"))

    #5
    def test_stacking_with_at(self):
        self.assertEqual(__, bold_and_italic_greet("Richard Wayne Gary Wayne"))

    #6
    def test_decorators_with_parameters(self):
        self.assertEqual(__, header_greet("Richard Wayne Gary Wayne"))

