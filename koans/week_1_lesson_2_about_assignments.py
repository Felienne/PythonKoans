from runner.koan import *

class AboutAssignments(Koan):
    
    # 1
    def test_integer_assignment(self):
        number_of_students = __
        self.assertEqual(137, number_of_students)

    # 2
    def test_integer_instance_of(self):
        number_of_students = __
        self.assertEqual(int, type(number_of_students))

    # 3
    def test_float_assignment(self):
        a_piece_of_pi = __
        self.assertEqual(3.14, a_piece_of_pi)

    # 4
    def test_float_instance_of(self):
        a_piece_of_pi = 3.14
        self.assertEqual(__, type(a_piece_of_pi))

    # 5
    def test_multi_assignment(self):
        first_prime, second_prime = 2, 3
        self.assertEqual(__, first_prime)
        self.assertEqual(__, second_prime)

    # 6
    def test_list_assignment(self):
        names = ["John", "Smith"]
        self.assertEqual(__, names)

    # 7
    def test_list_multi_assignments(self):
        first_name, last_name = ["John", "Smith"]
        self.assertEqual(__, first_name)
        self.assertEqual(__, last_name)

    # 8
    def test_parallel_assignments_with_extra_values(self):
        title, first_name, *last_name = ["Sir", "Guido", "van", "Rossum"]
        self.assertEqual(__, title)
        self.assertEqual(__, first_name)
        self.assertEqual(__, last_name)

    # 9
    def test_parallel_assignments_with_sublists(self):
        first_name, last_name = [["Billy", "Bob"], "Thornton"]
        self.assertEqual(__, first_name)
        self.assertEqual(__, last_name)

    # 10
    def test_swapping_with_parallel_assignment(self):
        first_minion = "Bob"
        last_minion = "Kevin"
        first_minion, last_minion = last_minion, first_minion
        self.assertEqual(__, first_minion)
        self.assertEqual(__, last_minion)



