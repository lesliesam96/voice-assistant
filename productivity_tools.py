import webbrowser
import subprocess
import platform
import os
import datetime
import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def authenticate_google_calendar():
    creds = None
    if os.path.exists('token.json'):
        with open('token.json', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def create_calendar_event(event_summary, start_time, end_time):
    creds = authenticate_google_calendar()
    service = build('calendar', 'v3', credentials=creds)

    event = {
        'summary': event_summary,
        'start': {
            'dateTime': start_time,
            'timeZone': 'Europe/Paris',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Europe/Paris',
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    return f"Event '{event_summary}' created on your Google Calendar."

def create_note(note_content):
    notes_folder = os.path.expanduser("~/Documents/VoiceAssistantNotes")
    os.makedirs(notes_folder, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(notes_folder, f"note_{timestamp}.txt")
    with open(filename, 'w') as file:
        file.write(note_content)
    return f"Note saved successfully as {filename}."

def set_reminder(reminder_content, remind_time):
    reminders_folder = os.path.expanduser("~/Documents/VoiceAssistantReminders")
    os.makedirs(reminders_folder, exist_ok=True)
    filename = os.path.join(reminders_folder, "reminders.txt")
    with open(filename, 'a') as file:
        file.write(f"{remind_time}: {reminder_content}\n")
    return f"Reminder '{reminder_content}' set for {remind_time}."

def close_all_windows():
    system_os = platform.system()
    if system_os == "Darwin":  # macOS
        subprocess.call(["osascript", "-e", 'tell application "System Events" to close windows of (every process whose visible is true)'])
        return "Closed all open windows on macOS."
    elif system_os == "Windows":
        subprocess.call(["taskkill", "/F", "/FI", "STATUS eq RUNNING"])
        return "Closed all open windows on Windows."
    elif system_os == "Linux":
        subprocess.call(["wmctrl", "-c", ":ACTIVE:"])
        return "Closed active windows on Linux."
    return "Unable to close windows on your operating system."

def open_gmail():
    webbrowser.open("https://mail.google.com/")
    return "Gmail has been opened in your browser."
