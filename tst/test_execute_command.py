import unittest
from unittest.mock import patch, MagicMock
from src.execute_command import ExecuteCommand
from typing import Optional

class TestExecuteCommand(unittest.TestCase):
    def setUp(self):
        """Setup a mock database manager and dependencies."""
        self.mock_db_manager = MagicMock()
        self.mock_gui_root = MagicMock()

        self.command_manager_patch = patch("src.execute_command.CommandManager", autospec=True)
        self.assistant_speaker_patch = patch("src.execute_command.AssistantSpeaker", autospec=True)

        self.mock_command_manager = self.command_manager_patch.start().return_value
        self.mock_assistant_speaker = self.assistant_speaker_patch.start().return_value

        self.executor = ExecuteCommand(self.mock_db_manager, self.mock_gui_root)

    def tearDown(self):
        """Stop all patches after each test."""
        self.command_manager_patch.stop()
        self.assistant_speaker_patch.stop()

    def test_execute_valid_command(self):
        """Test executing a valid command with a mapped function."""
        self.mock_db_manager.get_command_by_trigger.return_value = (1, "open_browser", "open browser")
        self.mock_command_manager.find_command_function.return_value = MagicMock()

        self.executor.execute("open browser")

        self.mock_command_manager.find_command_function.assert_called_with("open_browser")
        self.mock_assistant_speaker.announce_fulfillment.assert_called_with("open browser")

    def test_execute_unrecognized_command(self):
        """Test when an unrecognized command is given."""
        self.mock_db_manager.get_command_by_trigger.return_value = None

        with patch("builtins.print") as mock_print:
            self.executor.execute("non_existing_command")
            mock_print.assert_called_with("Command 'non_existing_command' not recognized.")

    def test_execute_command_with_no_function(self):
        """Test when a recognized command has no associated function."""
        self.mock_db_manager.get_command_by_trigger.return_value = (2, "unknown_command", "do something")
        self.mock_command_manager.find_command_function.return_value = None

        with patch("builtins.print") as mock_print:
            self.executor.execute("do something")
            mock_print.assert_called_with("No function found for 'unknown_command'.")

    def test_execute_command_with_function_exception(self):
        """Test when executing a command function raises an exception."""
        self.mock_db_manager.get_command_by_trigger.return_value = (3, "error_command", "cause error")
        mock_function = MagicMock(side_effect=Exception("Test Exception"))
        self.mock_command_manager.find_command_function.return_value = mock_function

        with patch("builtins.print") as mock_print:
            try:
                self.executor.execute("cause error")
            except Exception as e:
                mock_print.assert_called_with(f"Runtime error executing 'cause error': {e}")

    def test_execute_with_empty_command(self):
        """Test execution when an empty command is given."""
        with patch("builtins.print") as mock_print:
            self.executor.execute("")
            mock_print.assert_called_with("No command provided.")

            
if __name__ == "__main__":
    unittest.main()
