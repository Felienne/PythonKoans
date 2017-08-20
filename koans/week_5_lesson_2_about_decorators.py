from runner.koan import *

class FancyCat:
    def __init__(self, name, title):
        self._name = name
        self._title = title

    def get_name(self):
        return self._name

    def get_title(self):
        return self._title

class DecoratedCat:
    def __init__(self):
        self._name = None
        self._title = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name


class AboutDecorators(Koan):
    # 1
    def test_classes_can_have_private_fields(self):
        another_evil_cat = FancyCat("Mrs","Norris")
        self.assertEqual(__, another_evil_cat.get_name())
        self.assertEqual(__, another_evil_cat.get_title())


    #2
    def test_creating_properties_with_decorators_is_slightly_easier(self):
        another_evil_cat = DecoratedCat()

        another_evil_cat.name = "Cat Man Do"
        self.assertEqual(__, another_evil_cat.name)

