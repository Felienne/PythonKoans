from runner.koan import *


class Dog:
    """Dogs need regular walks. Never, ever let them drive."""
    age = 1

    def age_in_dog_years(self):
        return self.age * 7

class Bird:
    def __init__(self):
        self.age = 1

class Cat:
    __
    def __init__(self, n):
        self.name = n

    def what_am_I(self):
        return self

class FancyCat:
    def __init__(self, n, t):
        self.name = n
        self.title = t

    def get_full_name(self):
        return "{0}. {1}".format(__,self.name)

class Puppy:
    def give_food(self, food):
        return "Yum, I like {0}".format(food)

class Kitten:
    def __init__(self, favorite_food):
        self.favorite_food = favorite_food

    def give_food(self, food):
        if food == self.favorite_food:
            return "Yum!"
        else:
            return "Uuuuuuugh!"

class AI:
    def is_self_aware(self):
        return AI == type(self)

class Calculator:
    total = 0

    def add(self, value):
        self.total += value
        return self


class AboutClasses(Koan):
    #1
    def test_instances_of_classes_can_be_created_with_parentheses(self):
        fido = Dog()
        self.assertEqual(Dog, _________(fido))

    #2
    def test_classes_have_documentation_too(self):
        self.assertEqual(Dog.__doc__, __)

    #2
    def test_classes_have_documentation_too(self):
        self.assertEqual(Cat.__doc__, "Cats can walk themselves. Go away!")
        # Hint: Where is the blank for this Koan?

    def test_objects_have_data(self):
        fido = Dog()
        self.assertEqual(__, fido.age)

    def test_objects_have_methods(self):
        fido = Dog()
        self.assertEqual(__, fido.ageindogyears())

    def test_init_is_a_special_method(self):
        tweety = Bird()
        self.assertEqual(__, tweety.age)

    #4
    def test_init_method_can_also_take_data(self):
        felix = Cat("Felix Domestica Prima")
        self.assertEqual(__, felix.name)

    #6
    def test_methods_use_data(self):
        evil_cat = FancyCat("Mr.","Bigglesworth")
        self.assertEqual("Mr. Bigglesworth", evil_cat.get_full_name())
        # Hint: Where is the blank for this Koan?

    #7
    def test_different_objects_have_different_instance_variables(self):
        magically_evil_cat = FancyCat("Mrs", "Norris")
        evil_cat = FancyCat("Mr.","Bigglesworth")

        self.assertEqual(__, magically_evil_cat.title)
        self.assertEqual(__, evil_cat.name)

    def test_methods_can_take_parameters(self):
        fluffy = Puppy()
        self.assertEqual("Yum, I like potatoes", fluffy.give_food(__))

    def test_methods_can_take_parameters_and_use_data(self):
        garfield = Kitten("lasagna")
        self.assertEqual(__, garfield.give_food("potatoes"))
        self.assertEqual("Yum", garfield.give_food(__))

    #10--------------

    class Turtle:
        def __init__(self, n):
            self.name = n

    #11
    def test_classes_may_be_nested(self):
        sheldon = self.Turtle('Sheldon')
        self.assertEqual(__, type(sheldon))

    class Puppy:
        def give_food(self, food):
            return "More {0} please".format(food)

    #12
    def test_referencing_different_classes(self):
        beethoven = Puppy()
        fang = self.Puppy()

        self.assertEqual("Yum, I like shoes", beethoven.give_food(__))
        self.assertEqual(__, fang.give_food("shoes"))


    #13
    def test_what_is_self_here(self):
        self.assertEqual(__, type(self))

    #14
    def test_self_aware(self):
        alexa = AI()
        self.assertEqual(__, alexa.is_self_aware())

    #15
    def test_self_can_be_returned(self):
        c = Calculator()
        c.add(1).add(1).add(1)
        self.assertEqual(__, c.total)

    #16
    def test_type_of_return_self_is(self):
        c = Calculator()

        self.assertEqual(Calculator, _________(c.add(1)))

