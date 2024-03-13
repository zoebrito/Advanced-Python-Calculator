# plugin_interface.py
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from abc import ABC, abstractmethod

class PluginInterface(ABC):
    @abstractmethod
    def register_commands(self, command_handler):
        pass
