# app/app.py
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long

import os
import logging
import logging.config
import sys
from command_handler import CommandHandler
from plugin_interface import PluginInterface
from plugins.calculator_plugin import CalculatorPlugin

class App:
    def __init__(self):
        self.setup_logging()
        self.logger = logging.getLogger(__name__)  # Get the logger instance
        self.command_handler = CommandHandler()
        self.load_plugins()
        self.logger.info("Application started")
        self.logger.info("Available commands:")
        self.print_available_commands()  # Log available commands when the app starts
        print("Type 'exit' to exit.")

    def setup_logging(self):
        # Create a logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # Create a formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # Create a file handler
        file_handler = logging.FileHandler('app.log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        # Add handler to the logger
        self.logger.addHandler(file_handler)

        # Log a test message
        self.logger.info('Logging initialized')

    def load_plugins(self):
        plugins_dir = "plugins"
        if os.path.exists(plugins_dir) and os.path.isdir(plugins_dir):
            for filename in os.listdir(plugins_dir):
                if filename.endswith(".py") and filename != "__init__.py":
                    module_name = filename[:-3]
                    module = __import__(f"{plugins_dir}.{module_name}", fromlist=[module_name])
                    # Use direct import to access CalculatorPlugin class
                    plugin_class = module.CalculatorPlugin
                    if issubclass(plugin_class, PluginInterface):
                        plugin_instance = plugin_class()
                        plugin_instance.register_commands(self.command_handler)

    def start(self):
        while True:
            user_input = input(">>> ").strip().split()
            command_name = user_input[0]
            if command_name == 'exit':
                self.logger.info("Exiting program.")
                break
            try:
                args = [float(arg) for arg in user_input[1:]]
                result = self.command_handler.execute_command(command_name, args)
                log_message = f"User input: {user_input}, Result: {result}"
                self.logger.info(log_message)
                print("Result:", result)  # Print result to console
            except ValueError:
                self.logger.error("Invalid input. Please enter numbers.")

    def print_available_commands(self):
        available_commands = self.command_handler.get_available_commands()
        for command in available_commands:
            self.logger.info(f"- {command}")
            print(f"- {command}")

if __name__ == "__main__":
    app = App()
    app.start()
