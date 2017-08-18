from koans.week_1_lesson_2_about_assignments import AboutAssignments
from runner.koan import *


class AboutAssignmentsTest(Koan):
    # 1

    def test_koans(self):
        koan = AboutAssignments()
        self.assert_koan(137, koan.test_integer_assignment)

    def assert_koan(self, answer, koan):
        self.assert_currently_failing(koan)
        self.assert_correct_answer(answer, koan)

    def assert_correct_answer(self, answer, koan):
        global __
        reset = __
        __ = answer
        print("******* Answer is " + str(__))
        try:
            koan()
        finally:
            __ = reset

    def assert_currently_failing(self, koan):
        failed = False
        try:
            koan()
        except:
            failed = True
        self.assertTrue(failed, "The koan '{}' was left pre-answered".format(koan.__name__))