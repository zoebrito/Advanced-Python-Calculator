# tests/test_main.py
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

from unittest.mock import patch
from app import App

def test_app_start():
    # Define mock input function that returns predefined inputs
    mock_input = iter(["add 2 3", "subtract 5 2", "multiply 3 4", "divide 10 2", "exit"])

    # Initialize the App with mock input
    app = App(input_fn=lambda _: next(mock_input))

    # Start the app and capture the output
    output = []
    try:
        with patch('builtins.print',
                   side_effect=lambda *args: output.append(">>> " + " ".join(map(str, args)))):
            app.start()
    except OSError as e:  # Change Exception to a more specific exception like OSError
        assert False, f"Error occurred: {e}"

    # Print the output for inspection
    print("Output:", output)

    # Extract user input prompts from the output
    user_input_prompts = [item for item in output if item.startswith(">>> ")]

    # Add assertions to verify the user input prompts
    print("User input prompts:", user_input_prompts)

    # Update the expected output based on the actual output observed during the test execution
    expected_output = [
        ">>> Type 'exit' to exit.",
        ">>> 5.0",
        ">>> 3.0",
        ">>> 12.0",
        ">>> 5.0"
    ]

    # Add assertions to verify the user input prompts
    assert user_input_prompts == expected_output
