from config import LANGUAGE

from speech_to_text import transcribe_speech_whisper as transcribe_speech
from text_to_speech import speak
from command_executor import execute_command
from nlp_handler import get_response

def confirm_command(command):
    speak(f"I heard: '{command}'. Should I proceed?")
    print(f"Confirming command: '{command}'")
    confirmation = transcribe_speech()
    if confirmation:
        print(f"Confirmation received: {confirmation}")
        return any(yes_word in confirmation.lower() for yes_word in ["yes", "yeah", "sure", "proceed", "go ahead", "do it"])
    return False

def run_assistant():
    speak("Hello Leslie, how can I help you today?")
    while True:
        command = transcribe_speech()
        if command:
            print(f"Command received: {command}")

            if any(exit_word in command for exit_word in ["stop", "exit", "quit"]):
                speak("Assistant stopped. See you soon, Leslie!")
                break

            if confirm_command(command):
                response = execute_command(command)
                if response:
                    print(f"Command Response: {response}")
                    speak(response)
                else:
                    # Using NLP for unrecognized commands
                    nlp_response = get_response(command)
                    print(f"NLP Response: {nlp_response}")
                    speak(nlp_response)
            else:
                speak("Okay, let's try again.")

if __name__ == "__main__":
    run_assistant()
