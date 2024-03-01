# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        self.commands[name] = command

    def execute_command(self, name, args):
        if name in self.commands:
            return self.commands[name](args)

        print("Command not found.")
        return None  # or return a default value if necessary
