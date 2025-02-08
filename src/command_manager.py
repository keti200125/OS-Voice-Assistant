import webbrowser
import sys

class CommandManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get_all_commands(self):
        """Returns all commands from the database."""
        return self.db_manager.get_commands()

    def open_browser(self):
        """Opens a web browser."""
        print("Opening browser...")
        webbrowser.open("https://www.google.com")

    def play_music(self):
        """Plays music (dummy function for now)."""
        print("Playing music... (functionality to be implemented)")

    def close_program(self):
        """Closes the application."""
        print("Closing the program...")
        sys.exit()

    def show_commands(self):
        """Displays all available commands."""
        commands = self.get_all_commands()
        print("Available commands:")
        for _, command_name, trigger_phrase in commands:
            print(f"- {trigger_phrase} ({command_name})")

    def find_command_function(self, command_name):
        """Finds the corresponding function for a command."""
        command_map = {
            "open_browser": self.open_browser,
            "play_music": self.play_music,
            "close_program": self.close_program,
            "show_commands": self.show_commands
        }
        return command_map.get(command_name, None)
