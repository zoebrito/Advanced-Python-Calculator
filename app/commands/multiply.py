# app/commands/multiply.py
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

class MultiplyCommand:
    def execute(self, args):
        try:
            num1, num2 = map(float, args)
            result = num1 * num2
            return result
        except ValueError:
            print("Invalid input. Please provide two numbers.")
            return None
        