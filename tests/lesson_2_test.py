from koans import week_1_lesson_2_about_assignments
from koans.week_1_lesson_2_about_assignments import AboutAssignments
from runner.koan import Koan
from tests.koan_tester import KoanTester


class Lesson2Test(Koan):
    def test_lesson_2_assignments(self):
        tester = KoanTester(week_1_lesson_2_about_assignments, self);
        koan = AboutAssignments()
        tester.assert_koan(koan.test_integer_assignment, 137)
        tester.assert_koan(koan.test_integer_instance_of, 5)
        tester.assert_koan(koan.test_float_assignment, 3.14)
        tester.assert_koan(koan.test_float_instance_of, float)
        tester.assert_koan_2(koan.test_multi_assignment, 2, 3)
        tester.assert_koan(koan.test_list_assignment, "Smith")
        tester.assert_koan_2(koan.test_list_multi_assignments, "John","Smith")
        tester.assert_currently_failing(koan.test_parallel_assignments_with_extra_values)
        tester.assert_koan_2(koan.test_parallel_assignments_with_sublists, ["Billy","Bob"],"Thornton")
        tester.assert_koan_2(koan.test_swapping_with_parallel_assignment,"Kevin","Bob")

