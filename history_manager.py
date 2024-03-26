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
            logging.info(f"Loading calculation history from {self.history_file_path}")
            with open(self.history_file_path, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                history = list(reader)
            return history
        else:
            logging.warning("No calculation history found.")
            return []

    def save_history(self, history):
        with open(self.history_file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in history:
                writer.writerow(row)
        logging.info(f"Calculation history saved to {self.history_file_path}")

    def print_history(self):
        history = self.load_history()
        if history:
            logging.info("Calculation history:")
            for idx, row in enumerate(history, 1):
                logging.info(f"{idx}. {row}")
        else:
            logging.info("No calculation history available.")

    def remove_calculation(self, index):
        history = self.load_history()
        if history and index >= 1 and index <= len(history):
            removed_calculation = history.pop(index - 1)
            self.save_history(history)
            logging.info(f"Calculation {removed_calculation} removed from history.")
        else:
            logging.warning("Invalid index or no calculation history available.")
