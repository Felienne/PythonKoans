import unittest
__ = "-=> FILL ME IN! <=-"

class AboutLists(unittest.TestCase):

    # 1
    def test_creating_lists(self):
        empty_list = list()
        self.assertEqual(__, type(empty_list))
        self.assertEqual(__, len(empty_list))
        self.assertEqual(__, empty_list)

    # 2
    def test_list_creation(self):
        empty_list = list()
        self.assertEqual(__, empty_list)

        also_an_empty_list = []
        self.assertEqual(__, also_an_empty_list)

    # 3
    def test_list_assignment_and_append(self):
        nums = []
        nums[0:] = [1]
        nums[1:] = [2]
        self.assertListEqual(__, nums)

        nums.append(3)
        self.assertListEqual(__, nums)

    # 4
    def test_accessing_list_elements(self):
        beatles = ['John', 'Paul', 'George', 'Ringo']

        self.assertEqual(__, beatles[0])
        self.assertEqual(__, beatles[3])
        self.assertEqual(__, beatles[-1])
        self.assertEqual(__, beatles[-3])

    # 5
    def test_we_can_query_list_membership(self):
        beatles = ['John', 'Ringo', 'George', 'Paul']
        one_direction = ["Harry", "Niall", "Louis", "Liam", "Zayn"]

        self.assertEqual(__, 'John' in beatles )
        self.assertEqual(__, 'Ringo' not in one_direction)

    # 6
    def test_slicing_lists(self):
        beatles = ['John', 'Paul', 'George', 'Ringo']

        self.assertEqual(__, beatles[0:1])
        self.assertEqual(__, beatles[0:2])
        self.assertEqual(__, beatles[2:2])
        self.assertEqual(__, beatles[4:0])
        self.assertEqual(__, beatles[4:100])
        self.assertEqual(__, beatles[5:0])
        self.assertEqual(__, beatles[2:20])

    # 7
    def test_slicing_to_the_edge(self):
        beatles = ['John', 'Paul', 'George', 'Ringo']

        self.assertEqual(__, beatles[2:20])
        self.assertEqual(__, beatles[2:])
        self.assertEqual(__, beatles[0:2])
        self.assertEqual(__, beatles[0:])

    # 8
    def test_create_a_list_via_a_range(self):
        self.assertEqual(range, type(range(5)))

        self.assertEqual(__, list(range(5)))

        #note that ranges are not lists!
        self.assertNotEqual([0,1, 2, 3, 4], range(5))

    # 9
    def test_create_a_list_via_a_range_with_start(self):
        self.assertEqual(__, list(range(5, 9)))


    # 10
    def test_create_a_list_via_a_range_with_steps(self):
        self.assertEqual(__, list(range(0, 8, 2)))

        self.assertEqual(__, list(range(5, 1, -1)))
        self.assertEqual(__, list(range(1, 8, 3)))
        self.assertEqual(__, list(range(5, -7, -4)))
        self.assertEqual(__, list(range(5, -8, -4)))

    # 11
    def test_insertions(self):
        knight = ['you', 'will', 'pass']

        knight[1] = 'shall'
        self.assertEqual(__, knight)

        knight.insert(2, 'not')
        self.assertEqual(__, knight)

        knight.insert(0, 'Arthur')
        self.assertEqual(__, knight)

    # 12
    def test_popping_lists(self):
        stack = [1, 2, 3, 4]
        stack.append(5)

        self.assertEqual(__, stack)

        lucky_number = stack[4]
        self.assertEqual(__, lucky_number)
        self.assertEqual(__, stack)

        lucky_number = stack.pop()
        self.assertEqual(__, lucky_number)
        self.assertEqual(__, stack)


