# pylint: disable=missing-class-docstring

'''
Class that maintains calculation history

Uses class method which differs from static method in two ways:
Receives the class itself as the first parameter conventionally named 'cls'
Can access and modify class-level variables and class methods
'''

from decimal import Decimal
from typing import Callable, List

from calculator.calculations import Calculation

# makes a list of calcs called history + performs other functions
class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a new calculation to the history."""
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Retrieve the entire history of calculations."""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clear the history of calculations."""
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        """Get the latest calculation. Returns None if there's no history."""
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """Find and return a list of calculations by operation name."""
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]
    