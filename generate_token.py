import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow

# Scope for managing Google Calendar events
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def authenticate_google_calendar():
    creds = None
    if os.path.exists('token.json'):
        with open('token.json', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

        # Save the credentials into token.json
        with open('token.json', 'wb') as token:
            pickle.dump(creds, token)
            print("✅ token.json generated successfully!")

if __name__ == '__main__':
    authenticate_google_calendar()
