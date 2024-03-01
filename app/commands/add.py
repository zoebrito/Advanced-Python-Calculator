# app/commands/add.py
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

class AddCommand:
    def execute(self, args):
        try:
            num1, num2 = map(float, args)
            result = num1 + num2
            return result
        except ValueError:
            print("Invalid input. Please provide two numbers.")
            return None
        