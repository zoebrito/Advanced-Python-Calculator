# app/__init__.py
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

class App:
    def __init__(self, input_fn=input):
        self.input_fn = input_fn
        self.add_command = AddCommand()
        self.subtract_command = SubtractCommand()
        self.multiply_command = MultiplyCommand()
        self.divide_command = DivideCommand()

    def start(self):
        print("Type 'exit' to exit.")
        while True:
            user_input = self.input_fn(">>> ").strip()
            if not user_input:
                continue  # Skip empty input

            if user_input.lower() == 'exit':
                break  # Exit the loop if user inputs 'exit'

            # Split the input into command and arguments
            command, *args = user_input.split()
            self.process_command(command, args)

    def process_command(self, command, args):
        if command == 'add':
            result = self.add_command.execute(args)
        elif command == 'subtract':
            result = self.subtract_command.execute(args)
        elif command == 'multiply':
            result = self.multiply_command.execute(args)
        elif command == 'divide':
            result = self.divide_command.execute(args)
        else:
            print("Command not found.")
            return

        # Output the result if it's not None
        if result is not None:
            print(result)
