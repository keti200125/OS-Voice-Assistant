from src.command_manager import CommandManager
from src.assistant_speaker import AssistantSpeaker

class ExecuteCommand:
    def __init__(self, db_manager, gui_root=None):
        """Initializes the command executor with a database manager and optional GUI root."""
        self.command_manager = CommandManager(db_manager, gui_root)
        self.assistant_speaker = AssistantSpeaker()
        self.database_manager = db_manager  # Use the provided database manager instance

    def execute(self, command):
        """Finds and executes the corresponding function for a recognized command."""
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
                print(f"Error executing '{command}': {e}")
        else:
            print(f"No function found for '{command_name}'.")
