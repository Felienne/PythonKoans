
from runner.koan import *

class AboutFileIO(Koan):

    #2
    def test_reading_full_file(self):
        the_file = open("one_line.txt")
        contents = the_file.read()

        self.assertEqual(__, contents)

    #3
    def test_reading_file_with_multiple_lines(self):
        the_file = open("short_lines.txt")

        print(the_file)
        contents = the_file.read()

        self.assertEqual(__, contents)

    #4
    def test_reading_lines_directly(self):
        the_file = open("short_lines.txt")

        lines = the_file.readlines()

        self.assertEqual(__, lines)

    #5
    def test_reading_file_line_by_line(self):
        the_file = open("short_lines.txt")

        a_line = the_file.readline()
        self.assertEqual(__, a_line)

        another_line = the_file.readline()
        self.assertEqual(__, another_line)

        one_more = the_file.readline()
        self.assertEqual(__, one_more)

    #6
    def test_reading_file_with_for(self):
        the_file = open("short_lines.txt")

        lines = list()

        for line in the_file:
            lines.append(line)

        self.assertEqual(__, lines)

    #7
    def test_reading_file_with_for_strip(self):
        the_file = open("short_lines.txt")

        lines = list()

        for line in the_file:
            line = line.strip()
            lines.append(line)

        self.assertEqual(__, lines)


