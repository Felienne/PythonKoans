from runner.koan import *


class Dog:
    "Dogs need regular walks. Never, ever let them drive."

class Cat:
    def __init__(self, n):
        self.name = n

    def what_am_I(self):
        return self

class FancyCat:
    def __init__(self, n, t):
        self.name = n
        self.title = t

    def get_full_name(self):
        return "{0}. {1}".format(self.title,self.name)


class AboutClasses(Koan):
    #1
    def test_instances_of_classes_can_be_created_with_parentheses(self):
        fido = Dog()
        self.assertEqual(Dog, __)

    #2
    def test_classes_have_documentation_too(self):
        self.assertRegex(Dog.__doc__, __)

    #3
    def test_classes_are_types(self):
        self.assertEqual(__, self.Dog.__class__ == type)

    #4
    def test_init_method_creates_class(self):
        felix = Cat("Felix Domestica Prima")
        self.assertEqual(__, felix.name)

    #5
    def test_you_can_also_access_the_value_out_using_getattr_and_dict(self):
        felix = Cat("Felix Domestica Prima")
        self.assertEqual(__, felix.name)
        self.assertEqual(__, getattr(felix, "name"))


    #6
    def test_classes_can_have_methods(self):
        evil_cat = FancyCat("Mr.","Bigglesworth")
        self.assertEqual(__, evil_cat.get_full_name())

    #7
    def test_different_objects_have_different_instance_variables(self):
        evil_cat = FancyCat("Mr.","Bigglesworth")
        another_evil_cat = FancyCat("Mrs", "Norris")

        self.assertEqual(__, evil_cat.name == another_evil_cat.name)

    #9
    def test_self_returns_object(self):
        freckles = Cat('Freckles')
        self.assertEqual(__, type(freckles.what_am_I()))

    #10--------------

    class Turtle:
        def __init__(self, n):
            self.name = n

    #11
    def test_classes_may_be_nested(self):
        sheldon = self.Turtle('Sheldon')
        self.assertEqual(__, type(sheldon))

    #12
    def test_what_is_self_here(self):
        self.assertEqual(__, type(self))
