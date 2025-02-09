import sqlite3
import json
import os

class DatabaseManager:
    def __init__(self, db_name="assistant_data.db", json_file="commands.json", use_memory=False):
        """Initializes the database. Uses an in-memory database for testing if `use_memory=True`."""
        self.db_name = ":memory:" if use_memory else db_name
        self.json_file = json_file
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

        if not use_memory:
            self.add_default_commands()

    def create_table(self):
        """Creates the 'commands' table if it does not exist."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS commands (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            command_name TEXT UNIQUE, 
            trigger_phrase TEXT,      
            category TEXT
        )
        """)
        self.conn.commit()

    def load_commands_from_json(self):
        """Loads command data from the JSON file in the correct directory."""
        json_path = os.path.join(os.path.dirname(__file__), "commands.json")
        try:
            with open(json_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File '{json_path}' not found! Check the path.")
            return []
        except json.JSONDecodeError:
            print(f"Error reading '{json_path}'. Ensure the JSON format is valid!")
            return []

    def add_default_commands(self):
        """Adds predefined commands to the database if they do not already exist."""
        commands = self.load_commands_from_json()
        if not commands:
            return

        with self.conn:
            self.cursor.executemany(
                "INSERT OR IGNORE INTO commands (command_name, trigger_phrase, category) VALUES (:command_name, :trigger_phrase, :category)",
                commands
            )

    def add_command(self, command_name, trigger_phrase, category):
        """Adds a new command to the database."""
        try:
            with self.conn:
                self.cursor.execute(
                    "INSERT INTO commands (command_name, trigger_phrase, category) VALUES (?, ?, ?)",
                    (command_name, trigger_phrase, category)
                )
        except sqlite3.IntegrityError:
            print(f" Command '{command_name}' already exists!")

    def update_trigger_phrase(self, command_name, new_trigger_phrase):
        """Updates the trigger phrase of an existing command."""
        with self.conn:
            self.cursor.execute(
                "UPDATE commands SET trigger_phrase = ? WHERE command_name = ?",
                (new_trigger_phrase, command_name)
            )

    def get_commands(self):
        """Returns all stored commands."""
        self.cursor.execute("SELECT id, command_name, trigger_phrase FROM commands")
        return self.cursor.fetchall()

    def get_commands_by_category(self, category):
        """Fetches commands based on their category."""
        self.cursor.execute(
            "SELECT id, command_name, trigger_phrase FROM commands WHERE category = ?",
            (category,)
        )
        return self.cursor.fetchall()

    def delete_command(self, command_name):
        """Deletes a command from the database."""
        with self.conn:
            self.cursor.execute("DELETE FROM commands WHERE command_name = ?", (command_name,))

    def close_connection(self):
        """Closes the database connection."""
        self.conn.close()

    def get_command_by_trigger(self, trigger_phrase):
        """Fetches a command by its trigger phrase."""
        self.cursor.execute(
            "SELECT * FROM commands WHERE LOWER(trigger_phrase) = ?",
            (trigger_phrase.lower(),)
        )
        return self.cursor.fetchone()
