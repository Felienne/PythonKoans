#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based slightly on the lambdas section of AboutBlocks in the Ruby Koans
#

def make_order(order):
    return

from runner.koan import *

class AboutLambdas(Koan):
    def test_lambdas_can_be_assigned_to_variables_and_called_explicitly(self):
        add_one = lambda n: n + 1
        self.assertEqual(__, type(add_one))
        self.assertEqual(__, add_one(10))

    # ------------------------------------------------------------------

    def test_accessing_lambda_via_assignment(self):
        make_order = lambda qty: str(qty) + " " + order + "s"


        sausages = make_order('sausage')
        eggs = make_order('egg')

        self.assertEqual(__, sausages(3))
        self.assertEqual(__, eggs(2))

    def test_accessing_lambda_without_assignment(self):
        self.assertEqual(__, make_order('spam')(39823))
