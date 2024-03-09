# tests/test_main.py
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long

from unittest.mock import patch
from app.app import App

def test_app_start():
    # Define mock input values
    mock_inputs = ["add 2 3", "subtract 5 2", "multiply 3 4", "divide 10 2", "exit"]

    # Mock input function to return predefined inputs
    def mock_input(prompt):
        return mock_inputs.pop(0)

    # Initialize the App with mock input
    app = App()

    # Start the app and capture the output
    output = []
    try:
        with patch('builtins.input', side_effect=mock_input):
            with patch('builtins.print', side_effect=lambda *args, **kwargs: output.append(" ".join(map(str, args)))):
                app.start()
    except Exception as e:
        assert False, f"Error occurred: {e}"

    # Check if the program exited
    assert "Exiting program." in output

    # Assertions
    expected_output = [
        "Type 'exit' to exit.",
        "Result: 5.0",
        "Result: 3.0",
        "Result: 12.0",
        "Result: 5.0"
    ]
    assert output[:-1] == expected_output
