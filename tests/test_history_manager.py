# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import unittest
from history_manager import HistoryManager

class TestHistoryManager(unittest.TestCase):
    """
    Test cases for the HistoryManager class.
    """
    def setUp(self):
        self.history_manager = HistoryManager()

    def test_load_history(self):
        """
        Test loading calculation history.
        """
        history = self.history_manager.load_history()
        self.assertIsInstance(history, list)

    def test_save_history(self):
        """
        Test saving a calculation to history.
        """
        calculation = ["add", "2", "3", "5.0"]
        self.history_manager.save_history(calculation)
        history = self.history_manager.load_history()
        self.assertIn(calculation, history)

    def test_clear_history(self):
        """
        Test clearing the calculation history.
        """
        self.history_manager.clear_history()
        history = self.history_manager.load_history()
        self.assertEqual(len(history), 0)

if __name__ == '__main__':
    unittest.main()
