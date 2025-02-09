import unittest
from src.db_manager import DatabaseManager

class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        """Runs before each test - initializes an in-memory database."""
        self.db_manager = DatabaseManager(use_memory=True)

    def tearDown(self):
        """Runs after each test - closes the in-memory database."""
        self.db_manager.close_connection()

    def test_add_command(self):
        """Test adding a new command to the database."""
        self.db_manager.add_command("test_command", "say test", "test_category")
        commands = self.db_manager.get_commands()
        self.assertEqual(len(commands), 1)
        self.assertEqual(commands[0][1], "test_command")

    def test_update_trigger_phrase(self):
        """Test updating the trigger phrase of a command."""
        self.db_manager.add_command("update_test", "old phrase", "test_category")
        self.db_manager.update_trigger_phrase("update_test", "new phrase")
        commands = self.db_manager.get_commands()
        updated_command = [cmd for cmd in commands if cmd[1] == "update_test"][0]
        self.assertEqual(updated_command[2], "new phrase")

    def test_get_commands_by_category(self):
        """Test retrieving commands by category."""
        self.db_manager.add_command("cmd1", "trigger1", "category1")
        self.db_manager.add_command("cmd2", "trigger2", "category2")
        category1_commands = self.db_manager.get_commands_by_category("category1")
        self.assertEqual(len(category1_commands), 1)
        self.assertEqual(category1_commands[0][1], "cmd1")

    def test_delete_command(self):
        """Test deleting a command."""
        self.db_manager.add_command("delete_test", "trigger phrase", "test_category")
        self.db_manager.delete_command("delete_test")
        commands = self.db_manager.get_commands()
        self.assertEqual(len(commands), 0)

if __name__ == "__main__":
    unittest.main()
