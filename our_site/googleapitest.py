import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError

SCOPES = [
        "https://www.googleapis.com/auth/gmail.send"
]
flow = InstalledAppFlow.from_client_secrets_file("/Users/curtisbarnhart/Real curtisbarnhart/Schoolwork/2023-Fall/CS-130/westmont-cs130-f23-team-gold/our_site/client_secret_1040085023661-5l8q54odc68gaorivtfi1sdv4nvtsjig.apps.googleusercontent.com.json", SCOPES)
creds = flow.run_local_server(port=0)

service = build('gmail', 'v1', credentials=creds)
message = MIMEText('This is the body of the email')
message['to'] = 'cbarnhart@westmont.edu'
message['subject'] = 'Email Subject'
create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

try:
    message = (service.users().messages().send(userId="me", body=create_message).execute())
    print(F'sent message to {message} Message Id: {message["id"]}')
except HTTPError as error:
    print(F'An error occurred: {error}')
    message = None
