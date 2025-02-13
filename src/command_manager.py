"""
Command Manager module for handling system commands and opening web services.

This module provides a CommandManager class that interacts with the operating system
to open applications, websites, and perform system-related operations.
"""

import webbrowser
import os
from typing import Callable, Optional
from src.db_manager import DatabaseManager

WEB_URLS = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "gmail": "https://mail.google.com",
    "spotify": "https://open.spotify.com",
    "moodle": "https://learn.fmi.uni-sofia.bg/",
    "github_repo": "https://github.com/keti200125/OS-Voice-Assistant",
    "python_course": "https://github.com/keti200125/OS-Voice-Assistant"
}

SYSTEM_COMMANDS = {
    "open_notepad": "notepad",
    "open_calculator": "calc",
    "open_settings": "start ms-settings:",
    "open_file_explorer": "explorer",
    "open_task_manager": "taskmgr",
    "open_powershell": "start powershell",
    "open_control_panel": "control",
    "check_battery_status": "powercfg /batteryreport && start battery-report.html",
    "check_ip_address": "ipconfig",
    "check_disk_space": "wmic logicaldisk get size,freespace,caption",
    "check_running_processes": "tasklist",
    "check_system_uptime": "net stats srv"
}


class CommandManager:
    """Manages commands for opening applications, websites, and system utilities."""

    def __init__(self, db_manager: DatabaseManager, gui_root=None):
        """Initializes the CommandManager with a database manager and optional GUI root."""
        self.db_manager = db_manager
        self.gui_root = gui_root

    def get_all_commands(self) -> list:
        """Returns all available commands from the database."""
        return self.db_manager.get_commands()

    @staticmethod
    def open_url(url: str):
        """Opens a given URL in the default web browser, handling errors properly."""
        if not isinstance(url, str) or not url.startswith(("http://", "https://")):
            print(f"Invalid URL format: {url}")
            return
        try:
            webbrowser.open(url)
            print(f"Opening {url} in the browser...")
        except webbrowser.Error:
            print(f"Failed to open URL: {url} (Web browser error)")

    def open_website(self, site_name: str):
        """Opens a website based on its predefined name from the dictionary."""
        url = WEB_URLS.get(site_name.lower())
        if url:
            print(f"Opening {site_name.capitalize()}...")
            self.open_url(url)
        else:
            print(f"Unknown website: {site_name}")

    @staticmethod
    def run_system_command(command: str):
        """Runs a system command using os.system."""
        try:
            os.system(command)
        except FileNotFoundError:
            print(f"Error: Command '{command}' not found.")

    def execute_system_command(self, command_name: str):
        """Executes a system command from the predefined SYSTEM_COMMANDS dictionary."""
        command = SYSTEM_COMMANDS.get(command_name)
        if command:
            print(f"Executing {command_name}...")
            self.run_system_command(command)
        else:
            print(f"Unknown system command: {command_name}")

    def find_command_function(self, command_name: str) -> Optional[Callable]:
        """Finds and returns the corresponding function for a given command."""
        if command_name in WEB_URLS:
            return lambda: self.open_website(command_name)
        elif command_name in SYSTEM_COMMANDS:
            return lambda: self.execute_system_command(command_name)
        return getattr(self, command_name, None)
