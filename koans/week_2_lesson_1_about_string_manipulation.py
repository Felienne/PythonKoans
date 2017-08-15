from runner.koan import *

class AboutStringManipulation(Koan):

    #2
    def test_convert_an_int_to_string(self):
        winner = 65
        string = 'And the winner is...:' + str(winner)
        self.assertEqual(__, string)
        #try what happens without str around the number

    #3
    def test_use_format_to_print_nicer(self):
        winner = 65
        runner_up = 58
        string = "The top 2 is {0} and {1}".format(winner, runner_up)
        self.assertEqual(__, string)

    #4
    def test_formatted_values_can_be_shown_in_any_order_or_be_repeated(self):
        winner = 65
        runner_up = 58
        string = "The top 2 is {0} and {1}. I repeat... {0} then {1}!".format(winner, runner_up)
        self.assertEqual(__, string)

    #5
    def test_you_can_get_a_substring_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        self.assertEqual(__, string[7:10])

    #6
    def test_you_can_get_a_single_character_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        self.assertEqual(__, string[1])

    #7
    def test_single_characters_can_be_represented_by_integers(self):
        self.assertEqual(__, ord('a'))
        self.assertEqual(__, ord('b') == (ord('a') + 1))

    #8
    def test_strings_can_be_split(self):
        string = "Sausage Egg Cheese"
        words = string.split()
        self.assertListEqual([__, __, __], words)

    #9
    def test_strings_can_be_split_with_different_patterns(self):
        import re #import python regular expression library

        string = "the,rain;in,spain"
        pattern = re.compile(',|;')

        words = pattern.split(string)

        self.assertListEqual([__, __, __, __], words)

        # Pattern is a Python regular expression pattern which matches ',' or ';'

    #10
    def test_strings_can_be_joined(self):
        words = ["Now", "is", "the", "time"]
        self.assertEqual(__, ' '.join(words))

    #11
    def test_strings_can_change_case(self):
        self.assertEqual(__, 'guido'.capitalize())
        self.assertEqual(__, 'guido'.upper())
        self.assertEqual(__, 'TimBot'.lower())
        self.assertEqual(__, 'guido van rossum'.title())
        self.assertEqual(__, 'ToTaLlY aWeSoMe'.swapcase())
