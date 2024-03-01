# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long

import unittest
from app.commands.subtract import SubtractCommand

class TestSubtractCommand(unittest.TestCase):
    def test_subtract_command(self):
        subtract_command = SubtractCommand()

        result = subtract_command.execute(["5", "3"])
        self.assertEqual(result, 2)

        result = subtract_command.execute(["-2", "-3"])
        self.assertEqual(result, 1)

        result = subtract_command.execute(["0", "0"])
        self.assertEqual(result, 0)

    def test_subtract_command_invalid_input(self):
        subtract_command = SubtractCommand()

        result = subtract_command.execute(["6", "three"])  # Invalid input: second argument is not a number
        self.assertIsNone(result)  # Expecting None as result due to invalid input
