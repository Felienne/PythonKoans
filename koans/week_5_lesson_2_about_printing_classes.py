from runner.koan import *

class AboutPrintingClasses(Koan):
    class PrintableDog:
        def __init__(self, initial_name):
            self._name = initial_name

        def __str__(self):
            #
            # Implement this!
            #
            return __

        def __repr__(self):
            return "A dog named '" + self._name + "'"


    #1
    def test_str_provides_a_string_version_of_the_object(self):
        sue = self.PrintableDog("Sue")

        self.assertEqual("Sue", str(sue))

    #2
    def test_str_is_used_explicitly_in_string_interpolation(self):
        sue = self.PrintableDog("Sue")

        self.assertEqual(__, "My name is " + str(sue) + ". How do you do?")

    #3
    def test_repr_provides_a_more_complete_string_version(self):
        sue = self.PrintableDog("Sue")
        self.assertEqual(__, repr(sue))

    #4
    def test_all_objects_support_str_and_repr(self):
        seq = [1, 2, 3]

        self.assertEqual(__, str(seq))
        self.assertEqual(__, repr(seq))

        self.assertEqual(__, str("STRING"))
        self.assertEqual(__, repr("STRING"))
