
from runner.koan import *

def add(a, b):
    return a + b

def format_info(name, age = 18):
   """This returns the passed info as a nicely formatted string"""
   name_and_age_formatted = "{0} is currently {1} years old".format(name,age)

   return name_and_age_formatted

def pointless_method(a, b):
    sum = a + b

def empty_method():
    pass

def print_all_these(*args):
    to_print = ""
    for a in args:
        to_print += a + " "
    return to_print


class AboutFunctions(Koan):

    #1
    def test_calling_a_function(self):
        self.assertEqual(__, add(2, 3))

    #2
    def test_calling_with_default_values(self):
        self.assertEqual(__, format_info('Arnold', 70))
        self.assertEqual(__, format_info('Elle'))

    #3
    def test_calling_with_named_parameters(self):
        self.assertEqual(__, format_info(name = 'Chatum', Age=37))
        self.assertEqual(__, format_info(age = 47, name = 'Matthew'))

    #4
    def test_with_variable_number_of_arguments(self):
        self.assertEqual(__, print_all_these('Huey'))
        self.assertEqual(__, print_all_these('Huey','Dewey'))
        self.assertEqual(__, print_all_these('Huey','Dewey','Louie'))

    #5
    def test_function_too_can_have_documentation(self):
        self.assertEqual(__, format_info.__doc__)


    #6
    def test_function_too_needs_right_number_of_args(self):
        try:
            add()
        except TypeError as exception:
            msg = exception.args[0]

        self.assertEqual(__, msg)

        try:
            add(1, 2, 3)
        except Exception as e:
            msg = e.args[0]

        self.assertEqual(__, msg)

    #7
    def test_function_too_raises_on_wrong_number_of_args(self):
        with self.assertRaises(__):
            result = add(15, 29, 13)

    #8
    def test_function_which_does_not_return_anything(self):
        self.assertEqual(__, pointless_method(1, 2))

    #9
    def test_function_that_do_nothing_need_to_use_pass_as_a_filler(self):
        self.assertEqual(__, empty_method())




