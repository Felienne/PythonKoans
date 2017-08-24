def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def multiply_by_adding(a, b):
    total = 0
    for i in range(b):
        total = add(a, total)
    return total

def factorial(a):
    if a == 1:
        return 1
    else:
        return a * factorial(a-1)

def fibonacci(a):
    if a == 1:
        return __
    elif a == 2:
        return __
    else:
        return __ + __

from runner.koan import *

class AboutRecursion(Koan):

    #1
    def test_functions_can_call_each_other(self):
        self.assertEqual(__, multiply_by_adding(5,3))

    #2
    def test_functions_can_call_themselves(self):
        self.assertEqual(__, factorial(7))

    #3
    def test_recursive_function_can_have_more_base_cases(self):
        self.assertEqual(13, fibonacci(8))
        #hint: where is the blank for this koan?

