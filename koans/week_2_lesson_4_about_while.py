from runner.koan import *

class AboutWhile(Koan):

    #2
    def test_while_statement_string(self):
        digits = str()
        i = 0
        while i <= 10:
            digits = digits + str(i)
            i = i + 1
        self.assertEqual(__, digits)

    #3
    def test_while_statement_string_augmented_assignment(self):
        digits = str()
        i = 0
        while i <= 10:
            digits = digits + str(i)
            i += 1
        self.assertEqual(__, digits)


    #4
    def test_while_statement_sum_value(self):
        i = 1
        sum = 0
        while i <= 10:
            sum = sum + 1
            i += 1
        self.assertEqual(__, sum)


    #5
    def test_break_statement(self):
        i = 1
        sum = 0
        while True:
            sum = sum + 1
            i += 1

            if i > 10:
                break
        self.assertEqual(__, sum)


    #6
    def test_if_in_loop(self):
        i = 0
        even_numbers = []
        while i < 10:
            if (i % 2) == 0:
                even_numbers.append(i)
            i += 1
        self.assertEqual(__, even_numbers)


    #7
    def test_continue_statement(self):
        i = 0
        all_but_four = []
        while i < 6:
            i += 1
            if i == 4:
                continue

            all_but_four.append(i)

        self.assertEqual(__, all_but_four)

    #8
    def test_while_pop(self):

        all_letters= list("abcdef")
        reverse = []

        while all_letters != []:
            last_letter = all_letters.pop()

            reverse.append(last_letter)

        self.assertEqual(__, reverse)


    #9
    def test_while_pop_true(self):

        all_letters= list("abcdef")
        reverse = []

        while all_letters:
            last_letter = all_letters.pop()

            reverse.append(last_letter)

        self.assertEqual(__, reverse)


