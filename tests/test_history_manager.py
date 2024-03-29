# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long

import unittest
import pandas as pd
from history_manager import HistoryManager

class TestHistoryManager(unittest.TestCase):
    def setUp(self):
        self.history_manager = HistoryManager()

    def test_load_history_empty_file(self):
        # Test loading history from an empty file
        with open("history.csv", "w"):
            pass
        history = self.history_manager.load_history()
        self.assertIsInstance(history, pd.DataFrame)
        self.assertTrue(history.empty)

    def test_save_history_invalid_calculation(self):
        # Test saving an invalid calculation
        invalid_calculation = ("subtract", "5", "invalid_operand", "3")  # Invalid operand
        self.history_manager.save_history(invalid_calculation)
        history = self.history_manager.load_history()
        self.assertEqual(len(history), 0)  # Check that no invalid data was saved

    def test_save_history_multiple_calculations(self):
        # Test saving multiple calculations
        calculations = [("add", "2", "3", "5.0"), ("subtract", "5", "2", "3.0")]
        for calculation in calculations:
            self.history_manager.save_history(calculation)
        history = self.history_manager.load_history()
        self.assertEqual(len(history), len(calculations))

    def test_print_history(self):
        # Test printing the history
        calculation = ("multiply", "3", "4", "12.0")
        self.history_manager.save_history(calculation)
        with self.assertLogs() as log:
            self.history_manager.print_history()
            self.assertIn("Calculation history:", log.output[0])
            self.assertIn("User input: multiply 3 4, Result: 12.0", log.output[1])

    def test_clear_history_nonexistent_file(self):
        # Test clearing history when the file does not exist
        self.history_manager.clear_history()
        history = self.history_manager.load_history()
        self.assertEqual(len(history), 0)

    def test_clear_history_permission_error(self):
        # Test clearing history with a permission error
        with open("history.csv", "w"):
            pass  # Create a dummy file to cause a permission error
        # Set file permissions to read-only
        os.chmod("history.csv", 0o444)
        with self.assertLogs() as log:
            self.assertIsNone(self.history_manager.clear_history())
            self.assertIn("Permission denied to delete history file.", log.output[0])

    def test_load_history_error_handling(self):
        # Test error handling when loading history
        # Test FileNotFoundError
        with self.assertLogs() as log:
            with unittest.mock.patch("os.path.exists", return_value=False):
                self.assertIsInstance(self.history_manager.load_history(), pd.DataFrame)
                self.assertIn("No calculation history found.", log.output[0])
        # Test EmptyDataError
        with open("history.csv", "w"):
            pass  # Create an empty file
        with self.assertLogs() as log:
            self.assertIsInstance(self.history_manager.load_history(), pd.DataFrame)
            self.assertIn("Empty calculation history.", log.output[0])

if __name__ == '__main__':
    unittest.main()
