import unittest
from unittest.mock import patch, MagicMock
from src.command_manager import CommandManager
from src.db_manager import DatabaseManager


class TestCommandManager(unittest.TestCase):
    def setUp(self):
        """Създаваме mock на DatabaseManager и инициализираме CommandManager"""
        self.mock_db_manager = MagicMock(spec=DatabaseManager)
        self.cmd_manager = CommandManager(self.mock_db_manager)

    @patch("webbrowser.open")
    def test_open_url(self, mock_webbrowser):
        """Тества дали open_url() извиква webbrowser.open()"""
        url = "https://www.google.com"
        self.cmd_manager.open_url(url)
        mock_webbrowser.assert_called_once_with(url)

    @patch("os.system")
    def test_run_system_command(self, mock_os_system):
        """Тества дали run_system_command() извиква os.system() с правилната команда"""
        command = "notepad"
        self.cmd_manager.run_system_command(command)
        mock_os_system.assert_called_once_with(command)

    def test_find_command_function_valid(self):
        """Тества дали find_command_function() намира съществуваща команда"""
        func = self.cmd_manager.find_command_function("open_notepad")
        self.assertEqual(func, self.cmd_manager.open_notepad)

    def test_find_command_function_invalid(self):
        """Тества дали find_command_function() връща None за несъществуваща команда"""
        func = self.cmd_manager.find_command_function("non_existing_command")
        self.assertIsNone(func)


if __name__ == "__main__":
    unittest.main()
