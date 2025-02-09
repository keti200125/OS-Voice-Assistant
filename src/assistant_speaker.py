"""
This module provides text-to-speech functionality for the assistant.
"""
import time
import pyttsx3

class AssistantSpeaker:
    """Handles text-to-speech functionality for the assistant."""
    def __init__(self):
        """Initializes the speech engine."""
        self.engine = pyttsx3.init()

    def speak(self, text: str):
        """Pronounces the given text."""
        self.engine.say(text)
        self.engine.runAndWait()

    def greet_user(self, user_name: str):
        """Speaks a greeting to the user."""
        self.speak(f"Hello, {user_name}!")

    def announce_fulfillment(self, trigger_phrase: str):
        """Announces that the command has been executed."""
        time.sleep(2)
        self.speak(f"{trigger_phrase} is fulfilled")
