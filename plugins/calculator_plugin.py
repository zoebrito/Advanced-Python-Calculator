# app/plugins/calculator_plugin.py

from plugin_interface import PluginInterface

class CalculatorPlugin(PluginInterface):
    def register_commands(self, command_handler):
        command_handler.register_command("add", self.add_command)
        command_handler.register_command("subtract", self.subtract_command)
        command_handler.register_command("multiply", self.multiply_command)
        command_handler.register_command("divide", self.divide_command)

    def add_command(self, args):
        return args[0] + args[1]

    def subtract_command(self, args):
        return args[0] - args[1]

    def multiply_command(self, args):
        return args[0] * args[1]

    def divide_command(self, args):
        if args[1] == 0:
            return "Error: Division by zero"
        return args[0] / args[1]
