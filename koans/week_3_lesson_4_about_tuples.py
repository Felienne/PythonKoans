#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutTuples(Koan):

    #1
    def test_creating_a_tuple(self):
        count_of_three = (1, 2, 3)
        self.assertEqual(__, count_of_three[2])

    #2
    def test_tuples_are_immutable_so_item_assignment_is_not_possible(self):

        count_of_three = (1, 2, 3)
        try:
            count_of_three[2] = "three"
        except TypeError as ex:
            message = ex.args[0]
        self.assertEqual(message, __)
    #3
    def test_tuples_are_immutable_so_appending_is_not_possible(self):
        count_of_three =  (1, 2, 3)
        with self.assertRaises(___): count_of_three.append("boom")

    #4
    def test_tuples_can_only_be_changed_through_replacement(self):
        count_of_three = (1, 2, 3)

        list_count = list(count_of_three)
        list_count.append("boom")

        count_of_three = tuple(list_count)

        self.assertEqual(__, count_of_three)

    #5
    def test_tuples_of_one_look_peculiar(self):
        number_one = 1
        self.assertEqual(__, number_one.__class__)

        am_I_a_tuple = (1)
        self.assertEqual(__, am_I_a_tuple.__class__)

        or_am_I = (1,)
        self.assertEqual(__, or_am_I.__class__)

        tup1 = ("Imma tuple", )
        self.assertEqual(__, tup1.__class__)
        self.assertEqual(__, tup1)

    #6
    def test_tuple_constructor_can_be_surprising(self):
        self.assertEqual(__, tuple("Surprise!"))

    #7
    def test_creating_empty_tuples(self):
        self.assertEqual(__ , ())
        self.assertEqual(__ , tuple()) #Sometimes less confusing

    #8
    def test_tuples_can_be_nested(self):
        lat = (37, 14, 6, 'N')
        lon = (115, 48, 40, 'W')
        place = ('Area 51', lat, lon)
        self.assertEqual(__, place)


    #9
    def test_loop_over_tuples(self):
        print(type(("Lancelot", "Blue")))
        round_table = [
            ("Lancelot", "Blue"),
            ("Galahad", "I don't know!"),
            ("Robin", "Blue! I mean Green!"),
            ("Arthur", "Is that an African Sparrow or European Sparrow?")
        ]
        result = []
        for knight, answer in round_table:
            result.append("Contestant: '" + knight + "'   Answer: '" + answer + "'")

        self.assertEqual(result[0], __)
        self.assertEqual(result[1], __)
        self.assertEqual(result[2], __)
        self.assertEqual(result[3], __)



    #10
    def test_tuples_are_good_for_representing_records(self):
        locations = [
            ("Illuminati HQ", (38, 52, 15.56, 'N'), (77, 3, 21.46, 'W')),
            ("Stargate B", (41, 10, 43.92, 'N'), (1, 49, 34.29, 'W')),
        ]

        locations.append( ("Cthulu", (26, 40, 1, 'N'), (70, 45, 7, 'W')) )

        self.assertEqual(__, locations[2][0])
        self.assertEqual(__, locations[0][1][2])
