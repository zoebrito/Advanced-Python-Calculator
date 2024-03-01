# app/commands/divide.py
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=inconsistent-return-statements

class DivideCommand:
    def execute(self, args):
        try:
            num1, num2 = map(float, args)
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = num1 / num2
                return result
        except ValueError:
            print("Invalid input. Please provide two numbers.")
            return None # Return an expression (None) consistently
        