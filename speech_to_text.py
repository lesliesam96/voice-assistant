import whisper
import sounddevice as sd
import soundfile as sf
from config import LANGUAGE

def transcribe_speech_whisper():
    lang_code = LANGUAGE.split('-')[0]  # e.g., 'en' from 'en-US'
    fs = 44100
    seconds = 5  # Recording duration

    print(f"🎙️ Speak now ({seconds} seconds):")
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()

    audio_path = "input.wav"
    sf.write(audio_path, recording, fs)

    model = whisper.load_model("base")
    result = model.transcribe(audio_path, language=lang_code)
    text = result["text"]

    print("✅ Whisper recognized:", text)
    return text.lower().strip()
