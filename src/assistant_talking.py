import pyttsx3


def greet_user(user_name):
    """Speaks a greeting to the user."""
    engine = pyttsx3.init()
    engine.say(f"Hello, {user_name}!")
    engine.runAndWait()
