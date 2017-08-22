from koans.week_1_lesson_1_about_asserts import AboutAsserts
from koans import week_1_lesson_1_about_asserts
from koans.week_1_lesson_2_about_assignments import AboutAssignments
from koans import week_1_lesson_2_about_assignments
from koans.week_1_lesson_3_about_strings import AboutStrings
from koans import week_1_lesson_3_about_strings
from runner.koan import *


class KoanTest(Koan):
    def set(self, values):
        self.lesson.__ = values[0]
        self.lesson.______ = values[1]
        self.lesson._______ = values[2]

    def test_lesson_1_about_asserts(self):
        self.lesson = week_1_lesson_1_about_asserts
        koan = AboutAsserts()
        self.assert_currently_failing(koan.test_assert_truth)
        self.assert_currently_failing(koan.test_assert_with_message)
        self.assert_koan(koan.test_fill_in_values, 2)
        self.assert_koan(koan.test_assert_equality, 2)
        self.assert_koan(koan.test_a_better_way_of_asserting_equality, 2)

    def test_lesson_2_assignments(self):
        self.lesson = week_1_lesson_2_about_assignments

        koan = AboutAssignments()
        self.assert_koan(koan.test_integer_assignment, 137)
        self.assert_koan(koan.test_integer_instance_of, 5)
        self.assert_koan(koan.test_float_assignment, 3.14)
        self.assert_koan(koan.test_float_instance_of, float)
        self.assert_koan_2(koan.test_multi_assignment, 2, 3)

    def test_lesson_3_about_strings(self):
        self.lesson = week_1_lesson_3_about_strings
        koan = AboutStrings()
        self.assert_koan(koan.test_double_quoted_strings_are_strings, True)
        self.assert_koan(koan.test_print_something, "Hello class of 2017")
        self.assert_koan(koan.test_single_quoted_strings_are_also_strings, True)
        self.assert_koan(koan.test_triple_quote_strings_are_also_strings, True)
        self.assert_koan(koan.test_triple_single_quotes_work_too, True)
        self.assert_koan(koan.test_use_single_quotes_to_create_string_with_double_quotes, True)
        self.assert_koan(koan.test_use_double_quotes_to_create_strings_with_single_quotes, True)
        self.assert_koan(koan.test_use_backslash_for_escaping_quotes_in_strings, True)
        self.assert_koan(koan.test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line,  51)
        long_welcome = """
Howdy,
world!
"""
        self.assert_koan(koan.test_triple_quoted_strings_can_span_lines,  long_welcome)
        self.assert_koan(koan.test_triple_quoted_strings_need_less_escaping,  True)
        self.assert_koan(koan.test_plus_concatenates_strings,  "Lovelace")
        self.assert_koan(koan.test_adjacent_strings_are_concatenated_automatically,  "Lovelace")
        self.assert_koan_2(koan.test_plus_will_not_modify_original_strings,  "Love","lace")
        self.assert_koan(koan.test_plus_equals_will_append_to_end_of_string,  "Lovelace")


    def assert_koan(self, koan, answer):
        self.assert_any_koan(koan, [answer, None, None])

    def assert_koan_2(self, koan, answer1, answer2):
        self.assert_any_koan(koan, [None, answer1, answer2])

    def assert_any_koan(self, koan, answers):
        self.assert_currently_failing(koan)
        self.assert_correct_answer(answers, koan)

    def assert_correct_answer(self, answer, koan):
        reset = [__, ______, _______]
        self.set(answer)
        try:
            koan()
        finally:
            self.set(reset)

    def assert_currently_failing(self, koan):
        failed = False
        try:
            koan()
        except:
            failed = True
        self.assertTrue(failed, "The koan '{}' was left pre-answered".format(koan.__name__))
