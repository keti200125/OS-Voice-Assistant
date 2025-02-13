"""
Unit tests for the CommandManager class.

These tests ensure that web and system commands are executed correctly.
"""

import unittest
from unittest.mock import patch, MagicMock
from src.command_manager import CommandManager
from src.db_manager import DatabaseManager


class TestCommandManager(unittest.TestCase):
    """Test suite for the CommandManager class."""

    def setUp(self):
        """Sets up a mock database and initializes CommandManager."""
        self.mock_db = MagicMock(spec=DatabaseManager)
        self.mock_db.get_commands.return_value = [
            {
                "command_name": "open_google",
                "call_category": "web",
                "command_action": "https://www.google.com"
            },
            {
                "command_name": "open_notepad",
                "call_category": "system",
                "command_action": "notepad"
            }
        ]
        self.command_manager = CommandManager(self.mock_db)

    @patch("webbrowser.open")
    def test_open_url(self, mock_webbrowser):
        """Tests if URLs are opened correctly."""
        self.command_manager.open_url("https://www.example.com")
        mock_webbrowser.assert_called_once_with("https://www.example.com")

    @patch("os.system")
    def test_run_system_command(self, mock_os_system):
        """Tests if system commands execute correctly."""
        self.command_manager.run_system_command("notepad")
        mock_os_system.assert_called_once_with("notepad")

    @patch("webbrowser.open")
    def test_execute_web_command(self, mock_webbrowser):
        """Tests execution of web-related commands."""
        self.command_manager.execute_command("open_google")
        mock_webbrowser.assert_called_once_with("https://www.google.com")

    @patch("os.system")
    def test_execute_system_command(self, mock_os_system):
        """Tests execution of system-related commands."""
        self.command_manager.execute_command("open_notepad")
        mock_os_system.assert_called_once_with("notepad")

    def test_execute_unknown_command(self):
        """Tests behavior when executing an unknown command."""
        with patch("builtins.print") as mock_print:
            self.command_manager.execute_command("unknown_command")
            mock_print.assert_called_with("Unknown command: unknown_command")

    def test_run_invalid_system_command(self):
        """Test executing an invalid system command to trigger FileNotFoundError."""
        with patch("os.system", side_effect=FileNotFoundError):
            with patch("builtins.print") as mock_print:
                self.command_manager.run_system_command("invalid_command")
                mock_print.assert_called_with(
                    "Error: Command 'invalid_command' not found.")


if __name__ == "__main__":
    unittest.main()
