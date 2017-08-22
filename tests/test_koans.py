from koans.week_1_lesson_2_about_assignments import AboutAssignments
from koans import week_1_lesson_2_about_assignments
from runner import koan
from runner.koan import *



class KoanTest(Koan):
    def set(self, values):
        self.lesson.__ = values[0]
        self.lesson.______ = values[1]
        self.lesson._______ = values[2]

    def test_lesson_2_assignments(self):
        self.lesson = week_1_lesson_2_about_assignments

        koan = AboutAssignments()
        self.assert_koan(koan.test_integer_assignment, 137)
        self.assert_koan(koan.test_integer_instance_of, 5)
        self.assert_koan(koan.test_float_assignment, 3.14)
        self.assert_koan(koan.test_float_instance_of, float)
        self.assert_koan_2(koan.test_multi_assignment, 2, 3)


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