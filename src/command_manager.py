import webbrowser
import sys
import os


class CommandManager:
    def __init__(self, db_manager, gui_root=None):
        self.db_manager = db_manager
        self.gui_root = gui_root

    def get_all_commands(self):
        """Returns all commands from the database."""
        return self.db_manager.get_commands()

    def open_browser(self):
        """Opens a web browser."""
        print("Opening browser...")
        webbrowser.open("https://www.google.com")

    def open_youtube(self):
        """Opens YouTube in the default web browser."""
        webbrowser.open("https://www.youtube.com")
        print("Opening YouTube...")

    def open_gmail(self):
        """Opens Gmail."""
        print("Opening Gmail...")
        webbrowser.open("https://mail.google.com")

    def open_spotify(self):
        """Opens Spotify..."""
        print("Opening Spotify...")
        webbrowser.open("https://open.spotify.com")

    def open_moodle(self):
        """Opens Moodle..."""
        print("Opening moodle...")
        webbrowser.open("https://learn.fmi.uni-sofia.bg/")
    
    def open_github_repo(self):
        """Opens GitHub Repo of this project..."""
        print("Opening github repo...")
        webbrowser.open("https://github.com/keti200125/OS-Voice-Assistant")

    def open_settings(self):
        """Opens the Windows Settings application."""
        os.system("start ms-settings:")

    def open_file_explorer(self):
        """Opens the Windows File Manager."""
        os.system("explorer")

    def open_task_manager(self):
        """Opens the Windows Task Manager"""
        os.system("taskmgr")

    def open_powershell(self):
        """Opens Terminal"""
        os.system("start powershell")

    def play_music(self):
        """Plays music (dummy function for now)."""
        print("Playing music... (functionality to be implemented)")

    def close_program(self):
        """Closes the assistant application."""
        print("Shutting down the assistant...")
        if self.gui_root:
            self.gui_root.destroy()
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
            "open_youtube": self.open_youtube,
            "open_gmail": self.open_gmail,
            "open_spotify": self.open_spotify,
            "open_moodle": self.open_moodle,
            "open_github": self.open_github_repo,
            "play_music": self.play_music,
            "close_program": self.close_program,
            "show_commands": self.show_commands,
            "open_settings": self.open_settings,
            "open_file_explorer": self.open_file_explorer,
            "open_task_manager": self.open_task_manager,
            "open_powershell": self.open_powershell
        }
        return command_map.get(command_name, None)
