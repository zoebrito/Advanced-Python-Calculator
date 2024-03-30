# command_handler.py
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        self.commands[name] = command

    def execute_command(self, name, args=None):
        if name in self.commands:
            if args is not None:
                return self.commands[name](args)
            return self.commands[name]()
        return "Command not found"

    def get_available_commands(self):
        return list(self.commands.keys())
