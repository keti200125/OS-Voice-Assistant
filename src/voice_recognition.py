import threading
import speech_recognition as sr
from src.db_manager import DatabaseManager
from src.execute_command import ExecuteCommand


def recognize_speech(status_label=None):
    recognizer = sr.Recognizer()

    db_manager = DatabaseManager()

    execute_command = ExecuteCommand(db_manager)

    while True:
        with sr.Microphone() as source:
            print("Please speak...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio, language="en-US") # type: ignore
            command.lower()
            print(f"Recognized: {command}")
            execute_command.execute(command)

        except sr.UnknownValueError:
            print("Could not understand the command.")
        except sr.RequestError:
            print("There was a problem connecting to Google's server.")


def start_listening_thread():
    thread = threading.Thread(target=recognize_speech, args=(None,))
    thread.daemon = True
    thread.start()
