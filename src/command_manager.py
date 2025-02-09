import webbrowser
import sys
import os
from typing import Callable, Optional
from src.db_manager import DatabaseManager


class CommandManager:
    def __init__(self, db_manager: DatabaseManager, gui_root=None):
        """Initializes the CommandManager with a database manager and optional GUI root."""
        self.db_manager = db_manager
        self.gui_root = gui_root

    def get_all_commands(self) -> list:
        """Returns all available commands from the database."""
        return self.db_manager.get_commands()

    @staticmethod
    def open_url(url: str):
        """Opens a given URL in the default web browser."""
        try:
            webbrowser.open(url)
        except Exception as e:
            print(f"Error opening {url}: {e}")

    def open_browser(self):
        """Opens Google in the default web browser."""
        print("Opening browser...")
        self.open_url("https://www.google.com")

    def open_youtube(self):
        """Opens YouTube in the default web browser."""
        print("Opening YouTube...")
        self.open_url("https://www.youtube.com")

    def open_gmail(self):
        """Opens Gmail in the default web browser."""
        print("Opening Gmail...")
        self.open_url("https://mail.google.com")

    def open_spotify(self):
        """Opens Spotify in the default web browser."""
        print("Opening Spotify...")
        self.open_url("https://open.spotify.com")

    def open_moodle(self):
        """Opens Moodle in the default web browser."""
        print("Opening Moodle...")
        self.open_url("https://learn.fmi.uni-sofia.bg/")

    def open_github_repo(self):
        """Opens the GitHub repository of this project."""
        print("Opening GitHub repository...")
        self.open_url("https://github.com/keti200125/OS-Voice-Assistant")

    def open_python_course(self):
        """Opens the GitHub repository for the Python course."""
        print("Opening Python course repository...")
        self.open_url("https://github.com/keti200125/OS-Voice-Assistant")

    @staticmethod
    def run_system_command(command: str):
        """Runs a system command using os.system."""
        try:
            os.system(command)
        except Exception as e:
            print(f"Command failed: {e}")

    def open_notepad(self):
        """Opens Notepad."""
        print("Opening Notepad...")
        self.run_system_command("notepad")

    def open_calculator(self):
        """Opens the Calculator."""
        print("Opening Calculator...")
        self.run_system_command("calc")

    def open_settings(self):
        """Opens Windows Settings."""
        print("Opening Windows Settings...")
        self.run_system_command("start ms-settings:")

    def open_file_explorer(self):
        """Opens Windows File Explorer."""
        print("Opening File Explorer...")
        self.run_system_command("explorer")

    def open_task_manager(self):
        """Opens Windows Task Manager."""
        print("Opening Task Manager...")
        self.run_system_command("taskmgr")

    def open_powershell(self):
        """Opens Windows PowerShell."""
        print("Opening PowerShell...")
        self.run_system_command("start powershell")

    def open_control_panel(self):
        """Opens the Windows Control Panel."""
        print("Opening Control Panel...")
        self.run_system_command("control")

    def check_battery_status(self):
        """Displays battery status and generates a report."""
        print("Checking battery status...")
        self.run_system_command("powercfg /batteryreport && start battery-report.html")

    def check_ip_address(self):
        """Displays the computer's local IP address."""
        print("Checking IP address...")
        self.run_system_command("ipconfig")

    def check_disk_space(self):
        """Displays available and used disk space."""
        print("Checking disk space...")
        self.run_system_command("wmic logicaldisk get size,freespace,caption")

    def check_running_processes(self):
        """Lists all currently running processes."""
        print("Checking running processes...")
        self.run_system_command("tasklist")

    def check_system_uptime(self):
        """Displays how long the system has been running."""
        print("Checking system uptime...")
        self.run_system_command("net stats srv")

    def find_command_function(self, command_name: str) -> Optional[Callable]:
        """Finds and returns the corresponding function for a given command."""
        return getattr(self, command_name, None)
