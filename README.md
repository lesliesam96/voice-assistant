# Voice Assistant – Local AI Productivity Companion

A cross-platform voice assistant built in Python that can understand your speech, execute tasks locally, access Google Calendar, take notes, and answer general questions using Hugging Face LLMs.

---

## Features

- Speech recognition with OpenAI Whisper
- Text-to-speech using `pyttsx3`
- Command confirmation flow for reliability
- NLP integration with Hugging Face via LangChain
- Google Calendar event creation
- Local note-taking and reminders
- Gmail web access
- Fuzzy matching to handle pronunciation issues
- Packaged into a standalone desktop app (macOS)

---

## Requirements

- Python 3.11
- Virtualenv (recommended)

---

## Installation

```bash
git clone https://github.com/yourusername/voice-assistant.git
cd voice-assistant
python -m venv voice_assistant_env
source voice_assistant_env/bin/activate
pip install -r requirements.txt
```

---

## Project Structure

```
voice_assistant/
├── main.py
├── assistant.py
├── command_executor.py
├── speech_to_text.py
├── text_to_speech.py
├── nlp_handler.py
├── productivity_tools.py
├── config.py
├── credentials.json        # OAuth client from Google
├── token.json              # Generated automatically
├── requirements.txt
└── README.md
```

---

## Google Calendar Integration

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project.
3. Enable the **Google Calendar API**
4. Go to **Credentials** → Create OAuth client ID (Desktop app)
5. Download the `credentials.json` file and place it in the root of the project.
6. Run the following command once to generate `token.json`:

```bash
python generate_token.py
```

---

## NLP via Hugging Face

- You’ll need a Hugging Face API Token.
  1. Go to [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
  2. Create a token with "Read" permissions.
  3. Add it to `config.py`:

```python
HF_API_TOKEN = "your_token_here"
```

---

## Pack as Desktop App (macOS)

Install PyInstaller:

```bash
pip install pyinstaller
```

Then package the app:

```bash
pyinstaller --onefile --windowed --icon=voice_assistant.icns main.py
```

Move the app to Applications:

```bash
cp -r dist/main.app /Applications/VoiceAssistant.app
```

---

## Example Voice Commands

- "Open Gmail"
- "Search Google for machine learning"
- "Make a note call mom"
- "Set a reminder for lunch at 1pm"
- "Create calendar event team meeting"
- "What time is it?"
- "Stop"

---

## Credits

- [OpenAI Whisper](https://github.com/openai/whisper)
- [LangChain](https://github.com/hwchase17/langchain)
- [Hugging Face Transformers](https://huggingface.co)
- [Google Calendar API](https://developers.google.com/calendar)

---

## License

MIT License – Feel free to use, modify, and share!