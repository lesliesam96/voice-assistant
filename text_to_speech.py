import pyttsx3

from config import LANGUAGE

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Quick test
if __name__ == "__main__":
    speak("Hello Leslie, I'm ready to execute your commands.")

