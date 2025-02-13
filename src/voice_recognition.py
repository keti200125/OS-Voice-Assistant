"""
Voice recognition module for processing user speech commands.

This module uses speech recognition to convert spoken words into text
and execute appropriate commands.
"""

import threading
from typing import Optional
import speech_recognition as sr    # type: ignore
from src.db_manager import DatabaseManager
from src.execute_command import ExecuteCommand


def recognize_speech(_status_label: Optional[str] = None):
    """
    Continuously listens to user speech, converts it to text, and executes commands.
    Uses Google Speech Recognition to process spoken words and passes them to the 
    ExecuteCommand module for execution.
    """
    recognizer = sr.Recognizer()

    db_manager = DatabaseManager()
    execute_command = ExecuteCommand(db_manager)

    while True:
        with sr.Microphone() as source:
            print("Please speak...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio, language="en-US")  # type: ignore
            command.lower()
            print(f"Recognized: {command}")
            execute_command.execute(command)

        except sr.UnknownValueError:
            print("Could not understand the command.")
        except sr.RequestError:
            print("There was a problem connecting to Google's server.")


def start_listening_thread():
    """
    Starts a daemon thread that continuously listens for speech commands.
    This function runs `recognize_speech` in a separate thread to avoid blocking 
    the main program execution.
    """
    thread = threading.Thread(target=recognize_speech, args=(None,))
    thread.daemon = True
    thread.start()
