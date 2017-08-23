from koans import week_1_lesson_1_about_asserts
from koans.week_1_lesson_1_about_asserts import AboutAsserts
from runner.koan import *
from tests.koan_tester import KoanTester


class Lesson1Test(Koan):
    def test_lesson_1_about_asserts(self):
        tester = KoanTester(week_1_lesson_1_about_asserts, self);
        koan = AboutAsserts()
        tester.assert_currently_failing(koan.test_assert_truth)
        tester.assert_currently_failing(koan.test_assert_with_message)
        tester.assert_koan(koan.test_fill_in_values, 2)
        tester.assert_koan(koan.test_assert_equality, 2)
        tester.assert_koan(koan.test_a_better_way_of_asserting_equality, 2)


