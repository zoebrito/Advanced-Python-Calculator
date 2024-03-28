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
        try:
            open(self.history_file_path, 'a').close()  # Create the file if it doesn't exist
        except Exception as e:
            logging.error("Error creating history file: %s", e)

    def load_history(self):
        history = []
        try:
            if os.path.exists(self.history_file_path):
                logging.info("Loading calculation history from %s", self.history_file_path)
                with open(self.history_file_path, 'r', newline='', encoding='utf-8') as csvfile:
                    reader = csv.reader(csvfile)
                    history = list(reader)
                logging.info("Calculation history loaded successfully")
            else:
                logging.warning("No calculation history found.")
        except Exception as e:
            logging.error("Error loading calculation history: %s", e)
        return history

    def save_history(self, calculation):
        try:
            with open(self.history_file_path, 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(calculation)
            logging.info("Calculation saved to history.")
        except Exception as e:
            logging.error("Error saving calculation to history: %s", e)

    def print_history(self):
        history = self.load_history()
        if history:
            print("Calculation history:")
            for idx, record in enumerate(history, 1):
                command, *operands, result = record
                user_input = f"{command} {' '.join(operands)}"
                print(f"{idx}. User input: {user_input}, Result: {result}")
        else:
            print("No calculation history available.")

    def clear_history(self):
        if os.path.exists(self.history_file_path):
            os.remove(self.history_file_path)
            logging.info("Calculation history cleared.")
        else:
            logging.info("No calculation history found to clear.")
