import unittest
from unittest.mock import patch, MagicMock
from src.assistant_speaker import AssistantSpeaker


class TestAssistantSpeaker(unittest.TestCase):
    @patch("src.assistant_speaker.pyttsx3.init")
    def setUp(self, mock_pyttsx3):
        """Creates an instance of AssistantSpeaker with a mocked pyttsx3 engine."""
        self.mock_engine = MagicMock()
        mock_pyttsx3.return_value = self.mock_engine
        self.speaker = AssistantSpeaker() 

    def test_speak(self):
        """Tests if speak() calls pyttsx3.say() and runAndWait()."""
        self.speaker.speak("Test message")

        self.mock_engine.say.assert_called_once_with("Test message")
        self.mock_engine.runAndWait.assert_called_once()

    def test_greet_user(self):
        """Tests if greet_user() correctly says the greeting."""
        self.speaker.greet_user("Alice")

        self.mock_engine.say.assert_called_once_with("Hello, Alice!")
        self.mock_engine.runAndWait.assert_called_once()

    @patch("time.sleep", return_value=None)  
    def test_announce_fulfillment(self, _):
        """Tests if announce_fulfillment() correctly announces command execution."""
        self.speaker.announce_fulfillment("Open browser")

        self.mock_engine.say.assert_called_once_with("Open browser is fulfilled")
        self.mock_engine.runAndWait.assert_called_once()


if __name__ == "__main__":
    unittest.main()
