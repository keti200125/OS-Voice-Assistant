"""
Command Manager Module

This module provides functionality for managing system and web commands.
"""
import webbrowser
import os
import json
from typing import Callable, Optional
from src.db_manager import DatabaseManager


class CommandManager:
    """Manages commands for opening applications, websites, and system utilities."""

    def __init__(self, db_manager: DatabaseManager,
                 gui_root=None,
                 command_file="commands_action.json"):
        """Initializes the CommandManager with a db manager and optional GUI root."""
        self.db_manager = db_manager
        self.gui_root = gui_root
        self.commands = self.load_commands(command_file)

    @staticmethod
    def load_commands(command_file: str):
        """Loads commands from a JSON file."""
        try:
            with open(command_file, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading commands from {command_file}: {e}")
            return []

    def get_all_commands(self) -> list:
        """Returns all available commands from the JSON data."""
        return self.commands

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

    def execute_command(self, command_name: str):
        """Executes a command based on its category (web or system)."""
        command = next(
            (cmd for cmd in self.commands if cmd["command_name"] == command_name), None)
        if not command:
            print(f"Unknown command: {command_name}")
            return

        if command["call_category"] == "web":
            self.open_url(command["command_action"])
        elif command["call_category"] == "system":
            self.run_system_command(command["command_action"])
        else:
            print(f"Invalid command category: {command['call_category']}")

    @staticmethod
    def run_system_command(command: str):
        """Runs a system command using os.system."""
        try:
            os.system(command)
        except FileNotFoundError:
            print(f"Error: Command '{command}' not found.")

    def find_command_function(self, command_name: str) -> Optional[Callable]:
        """Finds and returns the corresponding function for a given command."""
        return lambda: self.execute_command(command_name)
