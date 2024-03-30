# tests/test_command_handler.py
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

from command_handler import CommandHandler

def test_execute_command_command_not_found():
    command_handler = CommandHandler()

    command_name = "invalid_command"
    args = []

    result = command_handler.execute_command(command_name, args)

    assert result == "Command not found"
    assert command_name not in command_handler.commands
