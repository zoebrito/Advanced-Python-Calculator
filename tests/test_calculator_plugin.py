# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name

import pytest
from command_handler import CommandHandler
from plugins.calculator_plugin import CalculatorPlugin

@pytest.fixture
def command_handler():
    return CommandHandler()

def test_calculator_plugin_register_commands(command_handler):
    plugin = CalculatorPlugin()
    plugin.register_commands(command_handler)
    assert "add" in command_handler.commands
    assert "subtract" in command_handler.commands
    assert "multiply" in command_handler.commands
    assert "divide" in command_handler.commands
    assert "clear" in command_handler.commands
    assert "history" in command_handler.commands
