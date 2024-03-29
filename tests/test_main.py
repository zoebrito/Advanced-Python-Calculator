# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long

import unittest
from unittest.mock import patch
from app.app import App

class TestApp(unittest.TestCase):
    def test_app_start(self):
        # Define mock input values
        mock_inputs = ["add 2 3", "subtract 5 2", "multiply 3 4", "divide 10 2", "exit"]

        # Mock input function to return predefined inputs
        def mock_input(prompt):
            return mock_inputs.pop(0)

        # Create an instance of the App class
        app = App()

        # Mock the setup_logging method to manually trigger logging initialization
        with patch.object(App, 'setup_logging'):
            # Start the app and capture the output
            output = []
            with patch('builtins.input', side_effect=mock_input):
                with patch('builtins.print', side_effect=lambda *args, **kwargs: output.append(" ".join(map(str, args)))):
                    app.start()

        # Assertions
        expected_output = [
            "Result: 5.0",
            "Result: 3.0",
            "Result: 12.0",
            "Result: 5.0"
        ]
        assert output == expected_output

if __name__ == '__main__':
    unittest.main()
