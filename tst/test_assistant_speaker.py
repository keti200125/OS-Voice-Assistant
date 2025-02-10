# """Unit tests for the AssistantSpeaker class."""

# import unittest
# from src.assistant_speaker import AssistantSpeaker
# from unittest.mock import patch, MagicMock


# class TestAssistantSpeaker(unittest.TestCase):
#     """Test cases for AssistantSpeaker class."""

#     def setUp(self) -> None:
#         """Creates an instance of AssistantSpeaker with a mocked pyttsx3 engine."""
#         with patch("src.assistant_speaker.pyttsx3.init") as mock_pyttsx3:
#             self.mock_engine: MagicMock = MagicMock()
#             mock_pyttsx3.return_value = self.mock_engine
#             self.speaker: AssistantSpeaker = AssistantSpeaker()

#     def test_speak(self) -> None:
#         """Tests if speak() calls pyttsx3.say() and runAndWait()."""
#         self.speaker.speak("Test message")

#         self.mock_engine.say.assert_called_once_with("Test message")
#         self.mock_engine.runAndWait.assert_called_once()

#     def test_speak_empty_string(self) -> None:
#         """Tests if speak() handles an empty string gracefully (should not speak)."""
#         self.speaker.speak("")

#         self.mock_engine.say.assert_not_called()
#         self.mock_engine.runAndWait.assert_not_called()

#     def test_greet_user(self) -> None:
#         """Tests if greet_user() correctly says the greeting."""
#         self.speaker.greet_user("Alice")

#         self.mock_engine.say.assert_called_once_with("Hello, Alice!")
#         self.mock_engine.runAndWait.assert_called_once()

#     @patch("time.sleep", return_value=None)
#     def test_announce_fulfillment(self, _: MagicMock) -> None:
#         """Tests if announce_fulfillment() correctly announces command execution."""
#         self.speaker.announce_fulfillment("Open browser")

#         self.mock_engine.say.assert_called_once_with("Open browser is fulfilled")
#         self.mock_engine.runAndWait.assert_called_once()


# if __name__ == "__main__":
#     unittest.main()
