import pyttsx3
import time

class AssistantSpeaker:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text):
        """Pronounces the given text."""
        self.engine.say(text)
        self.engine.runAndWait()

    def greet_user(self, user_name):
        """Speaks a greeting to the user."""
        self.speak(f"Hello, {user_name}!")

    def announce_fulfillment(self, trigger_phrase):
        """Announces that the command has been executed."""
        time.sleep(2)
        self.speak(f"{trigger_phrase} is fulfilled")