# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long

import unittest
from app.commands.add import AddCommand

class TestAddCommand(unittest.TestCase):
    def test_add_command(self):
        add_command = AddCommand()

        result = add_command.execute(["2", "3"])
        self.assertEqual(result, 5)

        result = add_command.execute(["-2", "3"])
        self.assertEqual(result, 1)

        result = add_command.execute(["0", "0"])
        self.assertEqual(result, 0)

    def test_add_command_invalid_input(self):
        add_command = AddCommand()

        result = add_command.execute(["2", "three"])  # Invalid input: second argument is not a number
        self.assertIsNone(result)  # Expecting None as result due to invalid input
