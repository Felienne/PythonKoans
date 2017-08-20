# ------------------------------------------------------------------

class Dog5:
    def __init__(self, initial_name):
        self._name = initial_name

    @property
    def name(self):
        return self._name


def test_init_provides_initial_values_for_instance_variables(self):
    fido = self.Dog5("Fido")
    self.assertEqual(__, fido.name)


def test_args_must_match_init(self):
    with self.assertRaises(___):
        self.Dog5()

        # THINK ABOUT IT: