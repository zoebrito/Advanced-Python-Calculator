'''
Basic operations file to reference in __init__.py
Uses type hinting to catch errors for parameters that don't match the type

'first_num: Decimal' and 'second_num: Decimal' in these functions indicate
that the parameters 'first_num" and "second_num' are expected to be of type decimal

'-> Decimal' indicates that the function returns a value of type decimal
'''

from decimal import Decimal

def add(first_num: Decimal, second_num: Decimal) -> Decimal:
    """Add two numbers"""
    return first_num + second_num

def subtract(first_num: Decimal, second_num: Decimal) -> Decimal:
    """Subtract two numbers"""
    return first_num - second_num

def multiply(first_num: Decimal, second_num: Decimal) -> Decimal:
    """Multiply two numbers"""
    return first_num * second_num

def divide(first_num: Decimal, second_num: Decimal) -> Decimal:
    """Divide two numbers"""
    if second_num == 0:
        raise ValueError("Cannot divide by zero") # error catch for dividing by 0
    return first_num / second_num
