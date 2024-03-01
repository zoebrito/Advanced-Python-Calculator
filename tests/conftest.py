# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import pytest
from faker import Faker
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

@pytest.fixture
def faker():
    return Faker()

@pytest.fixture
def generate_test_data(faker_data, num_records):
    test_data = []
    for _ in range(num_records):
        # Generate fake data for each record
        first_num = faker_data.random_number(digits=2)
        second_num = faker_data.random_number(digits=2)
        test_data.append((first_num, second_num))
    return test_data

@pytest.fixture
def add_command():
    return AddCommand()

@pytest.fixture
def subtract_command():
    return SubtractCommand()

@pytest.fixture
def multiply_command():
    return MultiplyCommand()

@pytest.fixture
def divide_command():
    return DivideCommand()
