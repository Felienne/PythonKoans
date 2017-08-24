from runner.koan import *

import functools

class AboutPartialApplication(Koan):
    def maximum(self, a, b):
        if a > b:
            return a
        else:
            return b

    #1
    def test_partial_function_applied_regularly(self):
        max = functools.partial(self.maximum)

        self.assertEqual(__, max(7, 23))
        self.assertEqual(__, max(10, -10))

    #2
    def test_partial__passing_first_arg(self):
        max_with_0 = functools.partial(self.maximum, 0)

        self.assertEqual(__, max_with_0(-4))
        self.assertEqual(__, max_with_0(5))

    #3
    def test_partial_that_wrappers_all_args(self):
        always_99 = functools.partial(self.maximum, 99, 20)
        always_20 = functools.partial(self.maximum, 9, 20)

        self.assertEqual(__, always_99())
        self.assertEqual(__, always_20())



