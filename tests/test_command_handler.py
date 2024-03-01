# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

import unittest
from app.commands import CommandHandler

def dummy_command(args):
    # Placeholder for args
    _ = args
    return "Dummy executed"

class TestCommandHandler(unittest.TestCase):
    def test_execute_command(self):
        handler = CommandHandler()

        # Register the proper function
        handler.register_command("dummy", dummy_command)

        # Test executing a registered command
        result = handler.execute_command("dummy", [])
        self.assertEqual(result, "Dummy executed")
