# tests/test_command_handler.py
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

from command_handler import CommandHandler

def test_execute_command_command_not_found():
    # Initialize the CommandHandler
    command_handler = CommandHandler()

    # Define a command name and args
    command_name = "invalid_command"
    args = []

    # Execute the command
    result = command_handler.execute_command(command_name, args)

    # Check if the result is "Command not found"
    assert result == "Command not found"

    # Check if the command name is not added to the commands dictionary
    assert command_name not in command_handler.commands
