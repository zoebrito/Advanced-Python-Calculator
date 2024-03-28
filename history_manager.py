# history_manager.py
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

import os
import logging
import csv

class HistoryManager:
    def __init__(self):
        self.history_file_path = os.path.abspath("history.csv")

    def load_history(self):
        if os.path.exists(self.history_file_path):
            logging.info("Loading calculation history from %s", self.history_file_path)
            with open(self.history_file_path, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                history = list(reader)
            return history
        logging.warning("No calculation history found.")
        return []

    def save_history(self, history):
        with open(self.history_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for row in history:
                writer.writerow(row)
        logging.info("Calculation history saved to %s", self.history_file_path)

    def print_history(self):
        history = self.load_history()
        if history:
            logging.info("Calculation history:")
            for idx, row in enumerate(history, 1):
                logging.info("%d. %s", idx, row)
        else:
            logging.info("No calculation history available.")

    def remove_calculation(self, index):
        history = self.load_history()
        if history and 1 <= index <= len(history):
            removed_calculation = history.pop(index - 1)
            self.save_history(history)
            logging.info("Calculation %s removed from history.", removed_calculation)
        else:
            logging.warning("Invalid index or no calculation history available.")
