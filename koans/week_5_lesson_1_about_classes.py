from runner.koan import *


class Dog:
    "Dogs need regular walks. Never, ever let them drive."

class Cat:
    def __init__(self, name):
        self.name = name

class FancyCat:
    def __init__(self, name, title):
        self.name = name
        self.title = name

    def get_full_name(self):
        return "{0}. {1}".format(self.title,self.name)

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


class AboutClasses(Koan):
    #1
    def test_instances_of_classes_can_be_created_adding_parentheses(self):
        fido = Dog()
        self.assertEqual(__, type(fido).__name__)
        self.assertEqual(__, type(fido))

    #2
    def test_classes_have_documentation_too(self):
        self.assertRegex(Dog.__doc__, __)

    #3 ------------------------------------------------------------------
    def test_init_method_is_the_constructor(self):
        felix = Cat("Felix Domestica Prima")
        self.assertEqual(__, felix.name)

    #4
    def test_you_can_also_access_the_value_out_using_getattr_and_dict(self):
        felix = Cat("Felix Domestica Prima")
        self.assertEqual(__, felix.name)
        self.assertEqual(__, getattr(felix, "name"))


    #5
    def test_classes_can_have_methods(self):
        evil_cat = FancyCat("Mr.","Bigglesworth")
        self.assertEqual(__, evil_cat.get_full_name())

    #6
    def test_different_objects_have_different_instance_variables(self):
        evil_cat = FancyCat("Mr.","Bigglesworth")
        another_evil_cat = FancyCat("Mrs", "Norris")

        self.assertEqual(__, evil_cat.name == another_evil_cat.name)

    # ------------------------------------------------------------------
    #7
    def test_str_provides_a_string_version_of_the_object(self):
        sue = PrintableDog("Sue")

        self.assertEqual("Sue", str(sue))

    #8
    def test_str_is_used_explicitly_in_string_interpolation(self):
        sue = PrintableDog("Sue")

        self.assertEqual(__, "My name is " + str(sue) + ". How do you do?")

    #9
    def test_repr_provides_a_more_complete_string_version(self):
        sue = PrintableDog("Sue")
        self.assertEqual(__, repr(sue))

    #10
    def test_all_objects_support_str_and_repr(self):
        seq = [1, 2, 3]

        self.assertEqual(__, str(seq))
        self.assertEqual(__, repr(seq))

        self.assertEqual(__, str("STRING"))
        self.assertEqual(__, repr("STRING"))
