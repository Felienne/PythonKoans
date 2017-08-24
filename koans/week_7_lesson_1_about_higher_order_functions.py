from runner.koan import *
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def apply(a,b, operator):
    return operator(a, b)

def greet(name):
    def get_message():
        return "Hello "

    result = get_message() + name
    return result

def add_constant(x):
    def addx(a):
        return a+x
    return addx


class AboutHigherOrderFunctions(Koan):


    #1
    def test_assigning_functions_to_variables(self):
        plus = add
        self.assertEqual(__, plus(5,7))

    #2
    def test_define_functions_in_other_functions(self):
        self.assertEqual(__, greet("John"))

    #3
    def test_functions_can_be_passed_as_parameters(self):
        self.assertEqual(__, apply(2,3,add))
        self.assertEqual(6, apply(2,3,__))

    #4
    def test_functions_can_return_functions(self):
        add5 = add_constant(5)
        self.assertEqual(__, add5(3))


