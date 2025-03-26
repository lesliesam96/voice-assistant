import subprocess
import webbrowser
import platform
from datetime import datetime
from fuzzywuzzy import fuzz
from productivity_tools import create_calendar_event, create_note, set_reminder, close_all_windows, open_gmail
import datetime


from config import LANGUAGE

def execute_command(command):
    system_os = platform.system()

    if any(keyword in command for keyword in ["open chrome", "open google", "launch browser", "google"]):
        if system_os == "Linux":
            subprocess.Popen(["google-chrome"])
        elif system_os == "Windows":
            subprocess.Popen(["start", "chrome"], shell=True)
        elif system_os == "Darwin":  # macOS
            subprocess.Popen(["open", "-a", "Google Chrome"])
        return "Google Chrome has been opened."

    elif any(keyword in command for keyword in ["visual studio code", "vs code", "code editor"]):
        subprocess.Popen(["code"])
        return "Visual Studio Code has been opened."

    elif "search" in command and "google" in command:
        query = command.split("google for")[-1].strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searching Google for {query}."
    
    
    elif "open gmail" in command:
        return open_gmail()

    elif "note" in command:
        note_content = command.split("note")[-1].strip()
        return create_note(note_content)

    elif "reminder" in command:
        reminder_content = command.split("reminder")[-1].strip()
        remind_time = (datetime.datetime.now() + datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M")
        return set_reminder(reminder_content, remind_time)

    elif "calendar event" in command or "schedule" in command:
        event_summary = command.split("event")[-1].strip()
        start_time = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%dT09:00:00")
        end_time = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%dT10:00:00")
        return create_calendar_event(event_summary, start_time, end_time)

    elif "close windows" in command or "close all" in command:
        return close_all_windows()
    

    elif any(keyword in command for keyword in ["time", "current time", "what time"]):
        current_time = datetime.now().strftime("%H:%M")
        return f"The current time is {current_time}."

    else:
        return None  # Command not recognized explicitly
