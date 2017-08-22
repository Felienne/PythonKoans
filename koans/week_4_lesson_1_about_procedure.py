
from runner.koan import *


def Adele_says_hello():
    print("Hello from the other side")

def Adele_says(line):
    """This method prints the inputted line"""
    print(line)

def Adele_one_liner(): print("How you doin?")

class AboutProcedures(Koan):

    #1
    def test_calling_a_method(self):

        i = 0
        while i < 5:
            Adele_says_hello()
            i +=1

        self.assertEqual(__, i)
        # look at the console!

    #2
    def test_calling_a_method_with_parameter(self):

        i = 0
        while i < 5:
            Adele_says("Singing line {0}".format(i))
            i +=1

        self.assertEqual(__, i)
        # look at the console!

    #3
    def test_the_documentation_can_be_viewed_with_the_doc_method(self):
        self.assertEqual(__, Adele_says.__doc__)

    #4
    def test_calling_method_with_wrong_number_of_arguments_messages(self):
        try:
            Adele_says()
        except TypeError as exception:
            msg = exception.args[0]

        self.assertEqual(__, msg)

        try:
            Adele_says(1, 2, 3)
        except Exception as e:
            msg = e.args[0]

        self.assertEqual(__, msg)


    #5
    def test_calling_method_with_wrong_number_of_arguments(self):
        with self.assertRaises(__):
            result = Adele_says("hello","and then some")

    #6
    def test_calling_a_one_line_method(self):

        i = 0
        while i < 12:
            Adele_one_liner()
            i +=1

        self.assertEqual(__, i)
        # look at the console!



