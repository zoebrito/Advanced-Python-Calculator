# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import

'''
Constructor with self parameter for calculator class
'''

# Import the Decimal class for precise decimal arithmetic
from decimal import Decimal
# Import Callable from typing to specify the operation as a callable type hint
from typing import Callable
# Import arithmetic operations from a module named calculator.operations
from calculator.operations import add, subtract, multiply, divide

# includes type hinting
class Calculation:
    def __init__(self, first_num: Decimal, second_num: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        # methods automatically converted by Python into MyClass.method(myobject, arg1, arg2)
        self.first_num = first_num
        self.second_num = second_num
        self.operation = operation  # Store the operation function

    # Static method to create a new instance of Calculation
    # This method provides an alternative constructor that can be used without instantiating the class directly
    @staticmethod
    def create(first_num: Decimal, second_num: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        # Return a new Calculation object initialized with the provided arguments
        return Calculation(first_num, second_num, operation)

    # Method to perform the calculation stored in this object
    def perform(self) -> Decimal:
        """Perform the stored calculation and return the result."""
        # The operation (e.g., add, subtract) is called with the operands (a and b) and the result is returned
        return self.operation(self.first_num, self.second_num)

    # Special method to provide a string representation of the Calculation instance
    def __repr__(self):
        """Return a simplified string representation of the calculation."""
        # This method makes it easier to understand what the Calculation object represents when printed or logged
        # The operation.__name__ attribute is used to get the function's name for a more readable output
        return f"Calculation({self.first_num}, {self.second_num}, {self.operation.__name__})"
    