from runner.koan import __, ______, _______


class KoanTester:
    def __init__(self, lesson, tester):
        self.lesson = lesson
        self.tester = tester

    def set(self, values):
        self.lesson.__ = values[0]
        self.lesson.______ = values[1]
        self.lesson._______ = values[2]

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
        self.tester.assertTrue(failed, "The koan '{}' was left pre-answered".format(koan.__name__))