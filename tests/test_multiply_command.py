# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long

import unittest
from app.commands.multiply import MultiplyCommand

class TestMultiplyCommand(unittest.TestCase):
    def test_multiply_command(self):
        multiply_command = MultiplyCommand()

        result = multiply_command.execute(["2", "3"])
        self.assertEqual(result, 6)

        result = multiply_command.execute(["-2", "3"])
        self.assertEqual(result, -6)

        result = multiply_command.execute(["0", "5"])
        self.assertEqual(result, 0)

    def test_multiply_command_invalid_input(self):
        multiply_command = MultiplyCommand()

        result = multiply_command.execute(["6", "three"])  # Invalid input: second argument is not a number
        self.assertIsNone(result)  # Expecting None as result due to invalid input
        