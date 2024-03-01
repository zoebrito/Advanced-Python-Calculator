# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long

import unittest
from app.commands.divide import DivideCommand

class TestDivideCommand(unittest.TestCase):
    def test_divide_command(self):
        divide_command = DivideCommand()

        result = divide_command.execute(["6", "3"])
        self.assertEqual(result, 2)

        result = divide_command.execute(["-6", "3"])
        self.assertEqual(result, -2)

        result = divide_command.execute(["0", "5"])
        self.assertEqual(result, 0)

    def test_divide_command_invalid_input(self):
        divide_command = DivideCommand()

        result = divide_command.execute(["6", "three"])  # Invalid input: second argument is not a number
        self.assertIsNone(result)  # Expecting None as result due to invalid input
        