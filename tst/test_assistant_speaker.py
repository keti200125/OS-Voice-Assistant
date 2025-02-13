"""
Unit tests for AssistantSpeaker class in assistant_speaker module.
"""

import unittest
from unittest.mock import MagicMock, patch
from src.assistant_speaker import AssistantSpeaker

class TestAssistantSpeaker(unittest.TestCase):
    """Tests for the AssistantSpeaker class."""

    def setUp(self):
        """Set up the AssistantSpeaker instance with a mocked speech engine."""
        with patch("src.assistant_speaker.pyttsx3.init", return_value=MagicMock()) as mock_init:
            self.mock_engine = mock_init.return_value
            self.speaker = AssistantSpeaker()

    def test_speak_calls_engine_say(self):
        """Test if speak() calls engine.say() with the correct text."""
        self.speaker.speak("Hello")
        self.mock_engine.say.assert_called_once_with("Hello")
        self.mock_engine.runAndWait.assert_called_once()

    def test_speak_does_not_speak_empty_text(self):
        """Test that speak() does not call engine.say() when given empty text."""
        self.speaker.speak("   ")
        self.mock_engine.say.assert_not_called()
        self.mock_engine.runAndWait.assert_not_called()

    def test_greet_user(self):
        """Test if greet_user() speaks the correct greeting."""
        self.speaker.greet_user("Alice")
        self.mock_engine.say.assert_called_once_with("Hello, Alice!")
        self.mock_engine.runAndWait.assert_called_once()

if __name__ == "__main__":
    unittest.main()
