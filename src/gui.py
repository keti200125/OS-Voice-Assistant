import threading
import tkinter as tk
from tkinter import messagebox
from src.db_manager import DatabaseManager
from src.voice_recognition import recognize_speech
from src.assistant_speaker import AssistantSpeaker


class AssistantGUI:
    def __init__(self):
        """Initializes the Voice Assistant GUI."""
        self.db = DatabaseManager()
        self.speaker = AssistantSpeaker()
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

        self.status_label = tk.Label(self.root, text="Assistant is not running.", fg="red")
        self.status_label.pack(pady=10)

        self.command_frame = tk.Frame(self.root)
        self.command_frame.pack(pady=10)

        self.root.mainloop()

    def start_assistant(self):
        """Starts the voice assistant and initializes speech recognition."""
        user_name = self.name_entry.get().strip()
        if not user_name:
            self.status_label.config(text="Please enter a name!", fg="red")
            return

        print(f"Hello, {user_name}!")
        self.speaker.greet_user(user_name)

        self.root.after(0, self.update_ui_after_start)

        def speech_thread():
            try:
                recognize_speech(user_name)
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("Error", f"Speech recognition failed: {e}"))

        threading.Thread(target=speech_thread, daemon=True).start()

    def update_ui_after_start(self):
        """Updates the UI after the assistant starts."""
        self.status_label.config(text="Assistant is running!", fg="green")
        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        self.start_button.pack_forget()
        self.show_category_list()

    def show_category_list(self):
        """Displays the category selection interface."""
        for widget in self.command_frame.winfo_children():
            widget.destroy()

        tk.Label(self.command_frame, text="Select Command Category", font=("Arial", 12)).pack(pady=5)

        categories = [("Web Applications", "applications"), 
                      ("Windows Utilities", "utilities"), 
                      ("System Management", "system")]

        button_frame = tk.Frame(self.command_frame)
        button_frame.pack(pady=5)

        [tk.Button(button_frame, text=label, command=lambda c=category: self.display_commands(c)).grid(row=0, column=i, padx=5, pady=5) 
         for i, (label, category) in enumerate(categories)]

    def display_commands(self, category):
        """Displays commands based on the selected category."""
        if hasattr(self, "current_category_frame"):
            self.current_category_frame.pack_forget()

        self.current_category_frame = tk.Frame(self.command_frame)
        self.current_category_frame.pack(pady=10)

        tk.Label(self.current_category_frame, text=f"{category.capitalize()} Commands", font=("Arial", 12)).pack(pady=5)

        self.command_entries = {}
        commands = self.db.get_commands_by_category(category)

        if not commands:
            tk.Label(self.current_category_frame, text="No commands available.", fg="red").pack(pady=5)

        frames = (self.create_command_entry_frame(command_name, trigger_phrase) for _, command_name, trigger_phrase in commands)
        for frame in frames:
            frame.pack(pady=2, padx=10, fill="x")

        tk.Button(self.current_category_frame, text="Save Changes", command=self.save_changes).pack(pady=10)
        tk.Button(self.current_category_frame, text="Back", command=self.show_category_list).pack(pady=5)

    def create_command_entry_frame(self, command_name, trigger_phrase):
        """Helper function to create entry frame for commands."""
        frame = tk.Frame(self.current_category_frame)

        tk.Label(frame, text=command_name, width=20, anchor="w").pack(side="left")

        entry = tk.Entry(frame, width=30)
        entry.insert(0, trigger_phrase)
        entry.pack(side="left", padx=5)

        self.command_entries[command_name] = entry
        return frame
    
    def save_changes(self):
        """Saves the updated trigger phrases in the database."""
        for command_name, entry in self.command_entries.items():
            new_trigger_phrase = entry.get().strip()
            if new_trigger_phrase:
                self.db.update_trigger_phrase(command_name, new_trigger_phrase)
        messagebox.showinfo("Success", "Commands have been updated!")


if __name__ == "__main__":
    AssistantGUI()
