# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long

import unittest
from unittest.mock import patch
from history_manager import HistoryManager

class TestHistoryManager(unittest.TestCase):
    @patch('history_manager.os.path.exists')
    @patch('history_manager.pd.read_csv')
    def test_load_history_exists(self, mock_pd_read_csv, mock_os_path_exists):
        mock_os_path_exists.return_value = True
        mock_pd_read_csv.return_value = None
        history_manager = HistoryManager()
        history_manager.load_history()
        mock_pd_read_csv.assert_called_once()

    @patch('history_manager.os.path.exists')
    def test_load_history_not_exists(self, mock_os_path_exists):
        mock_os_path_exists.return_value = False
        history_manager = HistoryManager()
        result = history_manager.load_history()
        self.assertTrue(result.empty)

    @patch('history_manager.os.path.exists')
    @patch('history_manager.os.remove')
    def test_clear_history_exists(self, mock_os_remove, mock_os_path_exists):
        mock_os_path_exists.return_value = True
        history_manager = HistoryManager()
        result = history_manager.clear_history()
        self.assertEqual(result, "cleared")
        mock_os_remove.assert_called_once_with(history_manager.history_file_path)

    @patch('history_manager.os.path.exists')
    def test_clear_history_not_exists(self, mock_os_path_exists):
        mock_os_path_exists.return_value = False
        history_manager = HistoryManager()
        result = history_manager.clear_history()
        self.assertIsNone(result)

    @patch('history_manager.os.path.exists')
    @patch('history_manager.os.remove')
    @patch('history_manager.logging')
    def test_clear_history_permission_error(self, mock_logging, mock_os_remove, mock_os_path_exists):
        mock_os_path_exists.return_value = True
        mock_os_remove.side_effect = PermissionError
        history_manager = HistoryManager()
        result = history_manager.clear_history()
        self.assertIsNone(result)
        mock_logging.error.assert_called_once()

    @patch('history_manager.os.path.exists')
    @patch('history_manager.os.remove')
    @patch('history_manager.logging')
    def test_clear_history_os_error(self, mock_logging, mock_os_remove, mock_os_path_exists):
        mock_os_path_exists.return_value = True
        mock_os_remove.side_effect = OSError
        history_manager = HistoryManager()
        result = history_manager.clear_history()
        self.assertIsNone(result)
        mock_logging.error.assert_called_once()

if __name__ == '__main__':
    unittest.main()
