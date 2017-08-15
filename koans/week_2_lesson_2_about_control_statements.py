from runner.koan import *

class AboutControlStatements(Koan):

    #2
    def test_if_then_else_statement_true_expression(self):
        threshold = 12
        if 5 < threshold:
            result = 'small enough'
        else:
            result = 'too big!'
        self.assertEqual(__, result)

    #3
    def test_if_then_else_statement_false_expression(self):
        threshold = 12
        if 28 < threshold:
            result = 'small enough'
        else:
            result = 'too big!'
        self.assertEqual(__, result)

    #4
    def test_if_then_else_statements_equals_expression(self):
        course_code = 'TI3105TU'

        if course_code == 'TI3105TU':
            result = 'yes!'
        else:
            result = 'this is not the course you are looking for'
        self.assertEqual(__, result)

    #5
    def test_if_then_else_statements_with_negated_expression(self):
        course_code = 'TI3105TU'

        if course_code != 'TI3105TU':
            result = 'oops, wrong course!'
        else:
            result = 'I want to learn Python'
        self.assertEqual(__, result)

    #6
    def test_if_then_only_statement(self):
        threshold = 12
        if 5 < threshold:
            result = 'small enough'
        self.assertEqual(__, result)

    #7
    def test_if_then_elif_else_statements(self):
        temperature = 5
        if temperature < 0:
            result = 'subzero'
        elif temperature == 0:
            result = 'zero'
        else:
            result = 'nice and warm'
        self.assertEqual(__, result)

