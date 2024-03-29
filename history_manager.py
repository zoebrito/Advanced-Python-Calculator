# history_manager.py
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long

import os
import logging
import pandas as pd

class HistoryManager:
    def __init__(self):
        self._initialize()

    def _initialize(self):
        self.history_file_path = os.path.abspath("history.csv")
        if not os.path.exists(self.history_file_path):
            try:
                with open(self.history_file_path, 'a', encoding='utf-8'):  # Specify encoding
                    pass  # Ensure file is created
            except OSError as e:
                logging.error("Error creating history file: %s", e)

    def load_history(self):
        try:
            if os.path.exists(self.history_file_path):
                logging.info("Loading calculation history from %s", self.history_file_path)
                history_df = pd.read_csv(self.history_file_path)
                logging.info("Calculation history loaded successfully")
            else:
                logging.warning("No calculation history found.")
                return pd.DataFrame(columns=["Command", "Operands", "Result"])
        except (FileNotFoundError, pd.errors.EmptyDataError) as e:  # Catch specific exceptions
            logging.error("Error loading calculation history: %s", e)
            return pd.DataFrame(columns=["Command", "Operands", "Result"])
        return history_df

    def save_history(self, calculation):
        try:
            command, *operands, result = calculation
            new_row = {"Command": command, "Operands": ' '.join(map(str, operands)), "Result": result}
            if os.path.exists(self.history_file_path):
                history_df = self.load_history()
                history_df = pd.concat([history_df, pd.DataFrame([new_row])], ignore_index=True)
            else:
                history_df = pd.DataFrame([new_row])
            history_df.to_csv(self.history_file_path, index=False)
            logging.info("Calculation saved to history.")
        except (TypeError, ValueError) as e:  # Catch specific exceptions
            logging.error("Error saving calculation to history: %s", e)

    def print_history(self):
        history_df = self.load_history()
        if not history_df.empty:
            print("Calculation history:")
            for idx, row in history_df.iterrows():
                command = row.get("Command", "")
                operands = row.get("Operands", "")
                result = row.get("Result", "")
                print(f"{idx+1}. User input: {command} {operands}, Result: {result}")
        else:
            print("No calculation history available.")

    def clear_history(self):
        if os.path.exists(self.history_file_path):
            try:
                os.remove(self.history_file_path)
                logging.info("Calculation history cleared.")
                return "cleared"
            except (PermissionError, OSError) as e:  # Catch specific exceptions
                logging.error("Error clearing calculation history: %s", e)
        else:
            logging.info("No calculation history found to clear.")
        return None
