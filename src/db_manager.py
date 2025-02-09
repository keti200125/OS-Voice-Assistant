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
            command_name TEXT UNIQUE, 
            trigger_phrase TEXT,      
            category TEXT
        )
        """)
        self.conn.commit()

    def add_default_commands(self):
        """Adds default commands to the database if they do not already exist."""
        default_commands = [
            ("open_browser", "open the browser", "apps"),
            ("open_youtube", "open youtube", "apps"),
            ("open_gmail", "open gmail", "apps"),
            ("open_spotify", "open spotify", "apps"),
            ("open_moodle", "open moodle", "apps"),
            ("open_github_repo", "open repo", "apps"),
            ("open_python_course", "open python", "apps"),

            ("close_program", "close the program", "system"),
            ("show_commands", "show the list of commands", "system"),
            ("open_settings", "open settings", "system"),
            ("open_file_explorer", "open file explorer", "system"),
            ("open_task_manager", "open task manager", "system"),
            ("open_powershell", "open powershell", "system")
        ]
        
        for command_name, trigger_phrase, category in default_commands:
            self.cursor.execute(
                "SELECT * FROM commands WHERE command_name = ?", (command_name,))
            result = self.cursor.fetchone()
            if not result:
                self.cursor.execute(
                    "INSERT INTO commands (command_name, trigger_phrase, category) VALUES (?, ?, ?)",
                    (command_name, trigger_phrase, category)
                )
        self.conn.commit()

    def add_command(self, command_name, trigger_phrase, category):
        """Adds a new command to the database."""
        self.cursor.execute(
            "INSERT INTO commands (command_name, trigger_phrase, category) VALUES (?, ?, ?)",
            (command_name, trigger_phrase, category)
        )
        self.conn.commit()

    def update_trigger_phrase(self, command_name, new_trigger_phrase):
        """Allows the user to update the trigger phrase."""
        self.cursor.execute(
            "UPDATE commands SET trigger_phrase = ? WHERE command_name = ?",
            (new_trigger_phrase, command_name)
        )
        self.conn.commit()
    
    def get_commands(self):
        """Returns only the required columns from the database."""
        self.cursor.execute("SELECT id, command_name, trigger_phrase FROM commands")
        return self.cursor.fetchall()

    
    def get_commands_by_category(self, category):
        """Fetches commands based on category."""
        self.cursor.execute(
            "SELECT id, command_name, trigger_phrase FROM commands WHERE category = ?",
            (category,)
        )
        return self.cursor.fetchall()

    def close_connection(self):
        """Closes the database connection."""
        self.conn.close()
