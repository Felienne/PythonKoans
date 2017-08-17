from koans.week_1_lesson_2_about_assignments import AboutAssignments
from runner.koan import *


class TestAboutAssignments(Koan):
    # 1

    def test_koans(self):
        failed = False
        try:
            AboutAssignments().test_integer_assignment()
        except:
            failed = True

        self.assertEqual(failed,True)
        x = __
        AboutAssignments().test_integer_assignment()