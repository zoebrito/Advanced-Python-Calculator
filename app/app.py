# app/app.py

import os
import logging
import logging.config
from command_handler import CommandHandler
from plugin_interface import PluginInterface
from plugins.calculator_plugin import CalculatorPlugin

class App:
    def __init__(self):
        self.setup_logging()  # Call the setup_logging method to configure logging
        self.command_handler = CommandHandler()
        self.load_plugins()

    def setup_logging(self):
        logging.config.fileConfig('logging.conf')  # Load logging configuration from logging.conf file

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
        print("Type 'exit' to exit.")
        while True:
            user_input = input(">>> ").strip().split()
            command_name = user_input[0]
            if command_name == 'exit':
                print("Exiting program.")
                break
            try:
                args = [float(arg) for arg in user_input[1:]]
                result = self.command_handler.execute_command(command_name, args)
                print("Result:", result)
            except ValueError:
                print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
    app = App()
    app.start()
