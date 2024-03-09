# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import pytest
from faker import Faker

@pytest.fixture
def faker():
    return Faker()

@pytest.fixture(params=[5, 10, 15])  # Change the values as needed
def num_records(request):
    return request.param
