#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutDefiningExceptions(Koan):

    class MySpecialError(RuntimeError):
        pass

    #TODO: uitsplitsen in meer tests
    #1
    def test_try_clause(self):
        result = None
        try:
            self.fail("Oops")
        except Exception as ex:
            result = 'exception handled'
            stored_exception = ex

        self.assertEqual(__, result)

        self.assertEqual(__, isinstance(stored_exception, Exception))
        self.assertEqual(__, isinstance(stored_exception, RuntimeError))

        self.assertTrue(issubclass(RuntimeError, __))

        self.assertEqual(__, stored_exception.args[0])

    #2
    def test_raising_a_specific_error(self):
        result = None
        try:
            raise self.MySpecialError("My Message")
        except self.MySpecialError as ex:
            result = 'exception handled'
            msg = ex.args[0]

        self.assertEqual(__, result)
        self.assertEqual(__, msg)

