from runner.koan import *

class AboutDictionaries(Koan):

    # 1
    def test_creating_dictionaries(self):
        empty_dict = dict()
        self.assertEqual(dict, type(empty_dict))
        self.assertDictEqual(__, empty_dict)
        self.assertEqual(__, len(empty_dict))

    # 2
    def test_dictionary_literals(self):
        babel_fish = {'one': 'uno', 'two': 'dos'}
        self.assertEqual(__, type(babel_fish))
        self.assertEqual(__, len(babel_fish))

    # 3
    def test_accessing_dictionaries(self):
        babel_fish = {'one': 'uno', 'two': 'dos'}
        self.assertEqual(__, babel_fish['one'])
        self.assertEqual(__, babel_fish['two'])

    # 4
    def test_changing_dictionaries(self):
        babel_fish = {'one': 'uno', 'two': 'dos'}
        babel_fish['one'] = 'eins'

        expected = {'one': __, 'two': 'dos'}
        self.assertDictEqual(expected, babel_fish)

    # 5
    def test_dictionary_is_unordered(self):
        dict1 = {'one': 'uno', 'two': 'dos'}
        dict2 = {'two': 'dos', 'one': 'uno'}
        self.assertEqual(__, dict1 == dict2)

    # 6
    def test_dictionary_keys_and_values(self):
        babel_fish = {'one': 'uno', 'two': 'dos'}
        self.assertEqual(__, len(babel_fish.keys()))
        self.assertEqual(__, len(babel_fish.values()))
        self.assertEqual(__, 'one' in babel_fish.keys())
        self.assertEqual(__, 'two' in babel_fish.values())
        self.assertEqual(__, 'uno' in babel_fish.keys())
        self.assertEqual(__, 'dos' in babel_fish.values())

    # 7
    def test_making_a_dictionary_from_a_sequence_of_keys(self):
        number_of_players = {}.fromkeys(('tennis', 'chess', 'Go'), 2)

        print(number_of_players)
        self.assertEqual(__, len(number_of_players))
        self.assertEqual(__, number_of_players['tennis'])
        self.assertEqual(__, number_of_players['Go'])

