from runner.koan import *

import functools

class AboutDecoratingWithClasses(Koan):
    def maximum(self, a, b):
        if a > b:
            return a
        else:
            return b

    def test_partial_that_wrappers_no_args(self):
        """
        Before we can understand this type of decorator we need to consider
        the partial.
        """
        max = functools.partial(self.maximum)

        self.assertEqual(__, max(7, 23))
        self.assertEqual(__, max(10, -10))

    def test_partial_that_wrappers_first_arg(self):
        max0 = functools.partial(self.maximum, 0)

        self.assertEqual(__, max0(-4))
        self.assertEqual(__, max0(5))

    def test_partial_that_wrappers_all_args(self):
        always99 = functools.partial(self.maximum, 99, 20)
        always20 = functools.partial(self.maximum, 9, 20)

        self.assertEqual(__, always99())
        self.assertEqual(__, always20())



