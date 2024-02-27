# pylint: disable=line-too-long
# pylint: disable=missing-docstring

# conftest.py
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):
    # Define operation mappings for both Calculator and Calculation tests
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    # Generate test data
    for _ in range(num_records):
        first_num = Decimal(fake.random_number(digits=2))
        second_num = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]
        # Ensure b is not zero for divide operation to prevent division by zero in expected calculation
        if operation_func == divide(first_num, second_num):
            second_num = Decimal('1') if second_num == Decimal('0') else second_num
        try:
            if operation_func == divide(first_num, second_num) and second_num == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(first_num, second_num)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        yield first_num, second_num, operation_name, operation_func, expected

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    # Check if the test is expecting any of the dynamically generated fixtures
    if {"first_num", "second_num", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        # Adjust the parameterization to include both operation_name and operation for broad compatibility
        # Ensure 'operation_name' is used for identifying the operation in Calculator class tests
        # 'operation' (function reference) is used for Calculation class tests.
        parameters = list(generate_test_data(num_records))
        # Modify parameters to fit test functions' expectations
        modified_parameters = [(first_num, second_num, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for first_num, second_num, op_name, op_func, expected in parameters]
        metafunc.parametrize("first_num,second_num,operation,expected", modified_parameters)
