import sqlite3


class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect("assistant_data.db")
        self.cursor = self.conn.cursor()
        self.create_table()
        self.add_default_commands()

    def create_table(self):
        """Creates a table for commands if it does not exist."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS commands (
            id INTEGER PRIMARY KEY,
            command_name TEXT UNIQUE,  -- Internal command name (e.g., "open_browser")
            trigger_phrase TEXT        -- User's trigger phrase (e.g., "open the browser")
        )
        """)
        self.conn.commit()

    def add_default_commands(self):
        """Adds default commands to the database if they do not already exist."""
        default_commands = [
            ("open_browser", "open the browser"),
            ("open_youtube", "open youtube"),
            ("open_gmail", "open gmail"),
            ("open_spotify", "open spotify"),
            ("open_moodle", "open moodle"),
            ("open_github_repo", "open repo"),
            ("play_music", "play music"),
            ("close_program", "close the program"),
            ("show_commands", "show the list of commands"),
            ("open_settings", "open settings"),
            ("open_file_explorer", "open file explorer"),
            ("open_task_manager", "open task manager"),
            ("open_powershell", "open powershell")
        ]
        for command_name, trigger_phrase in default_commands:
            self.cursor.execute(
                "SELECT * FROM commands WHERE command_name = ?", (command_name,))
            result = self.cursor.fetchone()
            if not result:
                self.cursor.execute(
                    "INSERT INTO commands (command_name, trigger_phrase) VALUES (?, ?)", (command_name, trigger_phrase))
        self.conn.commit()

    def add_command(self, command_name, trigger_phrase):
        """Adds a new command to the database."""
        self.cursor.execute(
            "INSERT INTO commands (command_name, trigger_phrase) VALUES (?, ?)", (command_name, trigger_phrase))
        self.conn.commit()

    def update_trigger_phrase(self, command_name, new_trigger_phrase):
        """Allows the user to update the trigger phrase."""
        self.cursor.execute(
            "UPDATE commands SET trigger_phrase = ? WHERE command_name = ?", (new_trigger_phrase, command_name))
        self.conn.commit()

    def get_commands(self):
        """Returns all commands from the database."""
        self.cursor.execute("SELECT * FROM commands")
        return self.cursor.fetchall()

    def close_connection(self):
        """Closes the database connection."""
        self.conn.close()
