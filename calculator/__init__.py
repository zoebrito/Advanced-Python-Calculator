# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long

"""
Calculator class that performs addition, subtraction, multiplication, and division
Uses static methods meaning it doesn't require an instance to be called
"""

# Import necessary modules and classes
from decimal import Decimal  # For high-precision arithmetic
from typing import Callable  # For type hinting callable objects
from calculator.calculation_history import Calculations  # Manages history of calculations
from calculator.operations import add, subtract, multiply, divide  # Arithmetic operations
from calculator.calculations import Calculation  # Represents a single calculation

# Definition of the Calculator class
class Calculator:
    @staticmethod
    def _perform_operation(first_num: Decimal, second_num: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, then return the result."""
        # Create a Calculation object using the static create method, passing in operands and the operation
        calculation = Calculation.create(first_num, second_num, operation)
        # Add the calculation to the history managed by the Calculations class
        Calculations.add_calculation(calculation)
        # Perform the calculation and return the result
        return calculation.perform()

    @staticmethod
    def add(first_num: Decimal, second_num: Decimal) -> Decimal:
        # Perform addition by delegating to the _perform_operation method with the add operation
        return Calculator._perform_operation(first_num, second_num, add)

    @staticmethod
    def subtract(first_num: Decimal, second_num: Decimal) -> Decimal:
        # Perform subtraction by delegating to the _perform_operation method with the subtract operation
        return Calculator._perform_operation(first_num, second_num, subtract)

    @staticmethod
    def multiply(first_num: Decimal, second_num: Decimal) -> Decimal:
        # Perform multiplication by delegating to the _perform_operation method with the multiply operation
        return Calculator._perform_operation(first_num, second_num, multiply)

    @staticmethod
    def divide(first_num: Decimal, second_num: Decimal) -> Decimal:
        # Perform division by delegating to the _perform_operation method with the divide operation
        return Calculator._perform_operation(first_num, second_num, divide)
