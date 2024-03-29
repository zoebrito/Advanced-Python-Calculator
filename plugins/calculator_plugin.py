# app/plugins/calculator_plugin.py
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from plugin_interface import PluginInterface
from history_manager import HistoryManager

class CalculatorPlugin(PluginInterface):
    def __init__(self):
        self.history_manager = HistoryManager()

    def register_commands(self, command_handler):
        command_handler.register_command("add", self.add_command)
        command_handler.register_command("subtract", self.subtract_command)
        command_handler.register_command("multiply", self.multiply_command)
        command_handler.register_command("divide", self.divide_command)
        command_handler.register_command("history", self.print_history)
        command_handler.register_command("clear", self.clear_history)

    def add_command(self, args):
        result = args[0] + args[1]
        self.history_manager.save_history(["add"] + args + [result])
        return result

    def subtract_command(self, args):
        result = args[0] - args[1]
        self.history_manager.save_history(["subtract"] + args + [result])
        return result

    def multiply_command(self, args):
        result = args[0] * args[1]
        self.history_manager.save_history(["multiply"] + args + [result])
        return result

    def divide_command(self, args):
        if args[1] == 0:
            result = "Error: Division by zero"
        else:
            result = args[0] / args[1]
        self.history_manager.save_history(["divide"] + args + [result])
        return result

    def print_history(self, args=None):
        self.history_manager.print_history()
        return None

    def clear_history(self, args=None):
        self.history_manager.clear_history()
        return None
