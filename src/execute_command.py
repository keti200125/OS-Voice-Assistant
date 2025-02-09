import webbrowser
import sys
from src.command_manager import CommandManager


class ExecuteCommand:
    def __init__(self, db_manager, gui_root=None):
        self.command_manager = CommandManager(db_manager, gui_root)

    def execute(self, command):
        """Finds and executes the function for the recognized command."""
        commands = self.command_manager.get_all_commands()

        for _, command_name, trigger_phrase in commands:
            if trigger_phrase.lower() == command.lower():
                command_function = self.command_manager.find_command_function(
                    command_name)
                if command_function:
                    command_function()
                    return

        print(f"Command '{command}' not recognized.")
