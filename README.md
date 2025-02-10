# OS-Voice-Assistant

OS Voice Assistant is a Python-based voice-controlled assistant that can recognize spoken commands and execute predefined actions. The project utilizes speech_recognition for speech processing and pyttsx3 for text-to-speech output.

## Features

* Listens for voice commands

* Modifies commands calls

* Recognizes and processes spoken text

* Executes predefined commands

* Provides spoken feedback

## Requirements

Before installing, make sure you have the following:

* Python 3.10 or later

* A working microphone

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/keti200125/OS-Voice-Assistant.git
cd OS-Voice-Assistant
```

### 2.Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate      # For Windows
```

### 3.Install Dependencies
```sh
pip install -r requirements.txt
```

## Running the Voice Assistant
```sh
python main.py
```

## **Project Structure**
```bash
📁 OS-Voice-Assistant/               # Root directory
│── 📁 src/                          # Source code
│   ├── __init__.py                  # Marks src/ as a package
│   ├── assistant_speaker.py         # Text-to-speech
│   ├── command_manager.py           # Manages voice commands
│   ├── db_manager.py                # Manages database
│   ├── execute_commands.py          # Executes voice commands
│   ├── gui.py                       # GUI
│   ├── voice_recognition.py         # Speech recognition
│── 📁 tst/                          # Unit tests
│   ├── __init__.py                  # Marks tst/ as a package
│   ├── test_assistant_speaker.py    # Tests for the assistant_speaker module
│   ├── test_command_manager.py      # Tests for the command_manager module
│   ├── test_db_manager.py           # Tests for the db_manager module
│   ├── test_execute_commands.py     # Tests for the execute_commands module
│── main.py                          # Main
│── commands.json                    # Predefined voice commands
│── requirements.txt                 # Dependencies
│── README.md                        # Project documentation
│── .gitignore                       # What to be ignored by Git
```
