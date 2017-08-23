from koans import week_1_lesson_3_about_strings
from koans.week_1_lesson_3_about_strings import AboutStrings
from runner.koan import Koan
from tests.koan_tester import KoanTester


class Lesson3Test(Koan):
    def test_lesson_3_about_strings(self):
        tester = KoanTester(week_1_lesson_3_about_strings, self);
        koan = AboutStrings()
        tester.assert_koan(koan.test_double_quoted_strings_are_strings, True)
        tester.assert_koan(koan.test_print_something, "Hello class of 2017")
        tester.assert_koan(koan.test_single_quoted_strings_are_also_strings, True)
        tester.assert_koan(koan.test_triple_quote_strings_are_also_strings, True)
        tester.assert_koan(koan.test_triple_single_quotes_work_too, True)
        tester.assert_koan(koan.test_use_single_quotes_to_create_string_with_double_quotes, True)
        tester.assert_koan(koan.test_use_double_quotes_to_create_strings_with_single_quotes, True)
        tester.assert_koan(koan.test_use_backslash_for_escaping_quotes_in_strings, True)
        tester.assert_koan(koan.test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line, 51)
        long_welcome = """
Howdy,
world!
"""
        tester.assert_koan(koan.test_triple_quoted_strings_can_span_lines, long_welcome)
        tester.assert_koan(koan.test_triple_quoted_strings_need_less_escaping, True)
        tester.assert_koan(koan.test_plus_concatenates_strings, "Lovelace")
        tester.assert_koan(koan.test_adjacent_strings_are_concatenated_automatically, "Lovelace")
        tester.assert_koan_2(koan.test_plus_will_not_modify_original_strings, "Love", "lace")
        tester.assert_koan(koan.test_plus_equals_will_append_to_end_of_string, "Lovelace")