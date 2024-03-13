# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long

import logging
from unittest.mock import patch
from app.app import App

def test_app_start(caplog):
    # Define mock input values
    mock_inputs = ["add 2 3", "subtract 5 2", "multiply 3 4", "divide 10 2", "exit"]

    # Mock input function to return predefined inputs
    def mock_input(prompt):
        return mock_inputs.pop(0)

    # Initialize the App with mock input
    app = App()

    # Start the app and capture the output
    output = []
    with patch('builtins.input', side_effect=mock_input):
        with patch('builtins.print', side_effect=lambda *args, **kwargs: output.append(" ".join(map(str, args)))):
            with caplog.at_level(logging.DEBUG):  # Capture log messages
                app.start()

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

    # Check log messages
    assert any(record.levelname == "INFO" and "Logging initialized" in record.message for record in caplog.records)
