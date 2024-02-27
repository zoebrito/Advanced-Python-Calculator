# pylint: disable=missing-docstring

from decimal import Decimal
import pytest
from calculator.calculations import Calculation
from calculator.operations import divide

@pytest.mark.filterwarnings("ignore:.*invalid-name.*")
def test_operation(first_num, second_num, operation, expected):
    '''Testing various operations'''
    calculation = Calculation.create(first_num, second_num, operation)
    assert calculation.perform() == expected, f"{operation.__name__} operation failed"

# Keeping the divide by zero test as is since it tests a specific case
def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()
