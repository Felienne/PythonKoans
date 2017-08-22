def make_order_for(foodtype):
    return lambda qty: str(qty) + " " + foodtype + "s"

from runner.koan import *

#TODO: needs some more koans still! not ready

class AboutLambdas(Koan):
    #1
    def test_lambdas_can_be_assigned_to_variables_and_called_explicitly(self):
        add_one = lambda n: n + 1
        self.assertEqual(__, type(add_one))
        self.assertEqual(__, add_one(10))

    #2
    def test_accessing_lambda_via_assignment(self):

        sausages = make_order_for('sausage')
        eggs = make_order_for('egg')

        self.assertEqual(__, sausages(3))
        self.assertEqual(__, eggs(2))

    #3
    def test_accessing_lambda_without_assignment(self):
        self.assertEqual(__, make_order_for('spam')(39823))
