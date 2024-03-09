# plugin_interface.py

from abc import ABC, abstractmethod

class PluginInterface(ABC):
    @abstractmethod
    def register_commands(self, command_handler):
        pass
