from runner.koan import *

class AboutStrings(Koan):

    def test_double_quoted_strings_are_strings(self):
        welcome = "Hello, world."
        self.assertEqual(__, isinstance(welcome, str))

    def test_print_something(self):
        welcome = "Hello class of 2017"

        print(welcome)

        #look at the console and compare with previous output
        self.assertEqual(__, welcome)


    def test_single_quoted_strings_are_also_strings(self):
        goodbye = 'Goodbye, world.'
        self.assertEqual(__, isinstance(goodbye, str))

    def test_triple_quote_strings_are_also_strings(self):
        welcome = """Howdy, world!"""
        self.assertEqual(__, isinstance(welcome, str))

    def test_triple_single_quotes_work_too(self):
        welcome = '''Bonjour tout le monde!'''
        self.assertEqual(__, isinstance(welcome, str))


    def test_use_single_quotes_to_create_string_with_double_quotes(self):
        quoted_sentence = 'He said, "Go Away."'
        self.assertEqual(__, isinstance(quoted_sentence, str))

    def test_use_double_quotes_to_create_strings_with_single_quotes(self):
        single_quoted_sentence = "Don't"
        self.assertEqual(__, isinstance(single_quoted_sentence, str))

    def test_use_backslash_for_escaping_quotes_in_strings(self):
        double_quoted_escape = "He said, \"Don't\""
        single_quoted_escape = 'He said, "Don\'t"'
        self.assertEqual(__, (double_quoted_escape == single_quoted_escape))

    def test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line(self):
        a_tale_of_two_lines = "It was the best of times,\
It was the worst of times."

        print(a_tale_of_two_lines)

        self.assertEqual(__, len(a_tale_of_two_lines))

    def test_triple_quoted_strings_can_span_lines(self):
        long_welcome = """
Howdy,
world!
"""
        self.assertEqual(15, len(long_welcome))

    def test_triple_quoted_strings_need_less_escaping(self):
        single_quoted_welcome = "Hello \"world\"."
        triple_quoted_welcome = """Hello "world"."""
        self.assertEqual(__, (a == b))

    def test_plus_concatenates_strings(self):
        first_programmer = "Love" + "lace"
        self.assertEqual(__, first_programmer)

    def test_adjacent_strings_are_concatenated_automatically(self):
        first_programmer = "Love" "lace"
        self.assertEqual(__, first_programmer)

    def test_plus_will_not_modify_original_strings(self):
        love = "Love"
        lace = "lace"
        first_programmer = love + lace
        self.assertEqual(__, love)
        self.assertEqual(__, lace)

    def test_plus_equals_will_append_to_end_of_string(self):
        love = "Love"
        lace = "lace"
        love += lace
        self.assertEqual(__, love)


