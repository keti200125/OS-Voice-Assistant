"""
This module provides text-to-speech functionality for the assistant.
"""

from time import sleep
import pyttsx3  # type: ignore


class AssistantSpeaker:
    """Handles text-to-speech functionality for the assistant."""

    def __init__(self) -> None:
        """Initializes the speech engine."""
        self.engine: pyttsx3.Engine = pyttsx3.init()

    def speak(self, text: str) -> None:
        """Pronounces the given text using the speech engine.
        Args:
            text (str): The text to be spoken.
        """
        if not text.strip():
            print("Warning: Attempted to speak empty text.")
            return
        self.engine.say(text)
        self.engine.runAndWait()

    def greet_user(self, user_name: str) -> None:
        """Speaks a greeting to the user.
        Args:
            user_name (str): The name of the user to greet.
        """
        self.speak(f"Hello, {user_name}!")

    def announce_fulfillment(self, trigger_phrase: str) -> None:
        """Announces that the command has been executed.
        Args:
            trigger_phrase (str): The phrase indicating the fulfilled command.
        """
        sleep(2)
        self.speak(f"{trigger_phrase} is fulfilled.")
