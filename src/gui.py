import pyttsx3
import threading
import tkinter as tk
from tkinter import messagebox
from src.db_manager import DatabaseManager
from src.voice_recognition import recognize_speech
from src.assistant_talking import greet_user


class AssistantGUI:
    def __init__(self):
        self.db = DatabaseManager()
        self.root = tk.Tk()
        self.root.title("Voice Assistant")
        self.root.geometry("500x500")

        self.name_label = tk.Label(self.root, text="Your Name:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.root, width=30)
        self.name_entry.pack(pady=5)

        self.start_button = tk.Button(
            self.root, text="Start Assistant", command=self.start_assistant)
        self.start_button.pack(pady=10)

        self.status_label = tk.Label(
            self.root, text="Assistant is not running.", fg="red")
        self.status_label.pack(pady=10)

        self.command_frame = tk.Frame(self.root)
        self.command_frame.pack(pady=10)

        self.root.mainloop()

    def start_assistant(self):
        """Starts the assistant."""
        user_name = self.name_entry.get().strip()
        if not user_name:
            self.status_label.config(text="Please enter a name!", fg="red")
            return

        print(f"Hello, {user_name}!")
        greet_user(user_name)

        self.status_label.config(text="Assistant is running!", fg="green")

        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        self.start_button.pack_forget()

        threading.Thread(target=recognize_speech, args=(
            user_name,), daemon=True).start()

        self.show_category_list()

    def show_category_list(self):
        """Displays the category selection interface."""
        for widget in self.command_frame.winfo_children():
            widget.destroy()

        tk.Label(self.command_frame, text="Select Command Category",
                 font=("Arial", 12)).pack(pady=5)

        tk.Button(self.command_frame, text="System Commands",
                  command=lambda: self.display_commands("system")).pack(pady=5)
        tk.Button(self.command_frame, text="Apps Commands",
                  command=lambda: self.display_commands("apps")).pack(pady=5)
        tk.Button(self.command_frame, text="System Management",
                  command=lambda: self.display_commands("management")).pack(pady=5)

    def display_commands(self, category):
        """Displays commands based on the selected category."""
        for widget in self.command_frame.winfo_children():
            widget.destroy()

        tk.Label(self.command_frame, text=f"{category.capitalize()} Commands", font=(
            "Arial", 12)).pack(pady=5)

        self.command_entries = {}
        commands = self.db.get_commands_by_category(category)

        if not commands:
            tk.Label(self.command_frame, text="No commands available.",
                     fg="red").pack(pady=5)

        for _, command_name, trigger_phrase in commands:
            frame = tk.Frame(self.command_frame)
            frame.pack(pady=2, padx=10, fill="x")

            tk.Label(frame, text=command_name, width=20,
                     anchor="w").pack(side="left")

            entry = tk.Entry(frame, width=30)
            entry.insert(0, trigger_phrase)
            entry.pack(side="left", padx=5)

            self.command_entries[command_name] = entry

        tk.Button(self.command_frame, text="Save Changes",
                  command=self.save_changes).pack(pady=10)
        tk.Button(self.command_frame, text="Back",
                  command=self.show_category_list).pack(pady=5)

    def save_changes(self):
        """Saves the updated commands in the database."""
        for command_name, entry in self.command_entries.items():
            new_trigger_phrase = entry.get()
            self.db.update_trigger_phrase(command_name, new_trigger_phrase)

        messagebox.showinfo("Success", "Commands have been updated!")
