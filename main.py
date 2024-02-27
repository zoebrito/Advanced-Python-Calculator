# pylint: disable=line-too-long
# pylint: disable=missing-docstring

import sys
from decimal import Decimal, InvalidOperation
from calculator import Calculator

class OperationCommand:
    def __init__(self, calculator, operation_name, first_num, second_num):
        self.calculator = calculator
        self.operation_name = operation_name
        self.first_num = first_num
        self.second_num = second_num

    def execute(self):
        # Retrieve the operation method from the Calculator class using getattr
        operation_method = getattr(self.calculator, self.operation_name, None)
        if operation_method:
            return operation_method(self.first_num, self.second_num)
        raise ValueError(f"Unknown operation: {self.operation_name}")

def calculate_and_print(first_num, second_num, operation_name):
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    # Unified error handling for decimal conversion
    try:
        a_decimal, b_decimal = map(Decimal, [first_num, second_num])
        result = operation_mappings.get(operation_name) # Use get to handle unknown operations
        if result:
            print(f"The result of {first_num} {operation_name} {second_num} is equal to {result(a_decimal, b_decimal)}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {first_num} or {second_num} is not a valid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError as e:
        print(e)


def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)
    _, first_num, second_num, operation = sys.argv
    calculate_and_print(first_num, second_num, operation)

if __name__ == '__main__':
    main()
