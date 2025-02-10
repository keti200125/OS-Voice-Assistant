"""
Module for executing recognized voice commands.

This module provides an ExecuteCommand class to handle 
retrieving and executing voice commands using a database manager.
"""

from typing import Optional
from src.command_manager import CommandManager
from src.assistant_speaker import AssistantSpeaker
from src.db_manager import DatabaseManager


class ExecuteCommand:
    """Handles the execution of recognized voice commands."""

    def __init__(self, db_manager: DatabaseManager, gui_root: Optional[object] = None) -> None:
        """
        Initializes the command executor with a database manager and optional GUI root.

        :param db_manager: The database manager instance for retrieving commands.
        :param gui_root: Optional GUI root for applications with a user interface.
        """
        self.command_manager = CommandManager(db_manager, gui_root)
        self.assistant_speaker = AssistantSpeaker()
        self.database_manager = db_manager

    def execute(self, command: str) -> None:
        """
        Finds and executes the corresponding function for a recognized command.

        :param command: The voice command to execute.
        """
        if not command:
            print("No command provided.")
            return

        matched_command = self.database_manager.get_command_by_trigger(command.lower())

        if not matched_command:
            print(f"Command '{command}' not recognized.")
            return

        command_name = matched_command[1]
        command_function = self.command_manager.find_command_function(command_name)

        if command_function:
            try:
                command_function()
                self.assistant_speaker.announce_fulfillment(command.lower())
            except Exception as e:
                print(f"Runtime error executing '{command}': {e}")
        else:
            print(f"No function found for '{command_name}'.")

    def validate_command(self, command: str) -> bool:
        """
        Validates whether a command exists in the database.

        :param command: The voice command to validate.
        :return: True if the command exists, otherwise False.
        """
        return bool(self.database_manager.get_command_by_trigger(command.lower()))
