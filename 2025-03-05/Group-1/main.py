# idea - Email a collection of data brokers with GDPR requests
import requests #fela's code - do not plagiarise

import base64
from email.message import EmailMessage

from os import getenv as get_env

sending_from_email = get_env("USER_EMAIL")
print(sending_from_email)
if sending_from_email is None:
  sending_from_email = open("my_email.txt").read().strip()

email_contents = open("email_contents.txt").read()

def create_email():
  message = EmailMessage()
  message.set_content(email_contents)

  # replace with email from reader.py
  message["To"] = "gduser1@workspacesamples.dev"
  
  message["From"] = sending_from_email
  message["Subject"] = "GDPR Right to be forgotten"

  # encoded message
  encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

  return {"raw": encoded_message}

if __name__ == "__main__f":
  print(create_email())

# pip import python-gmail

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def gmail_send_message():
  """Create and send an email message
  Print the returned  message id
  Returns: Message object, including message id

  Load pre-authorized user credentials from the environment.
  TODO(developer) - See https://developers.google.com/identity
  for guides on implementing OAuth2 for the application.
  """
  creds, _ = google.auth.default()

  try:
    service = build("gmail", "v1", credentials=creds)
    create_message = create_email()

    send_message = (
        service.users()
        .messages()
        .send(userId="me", body=create_message)
        .execute()
    )
    print(f'Message Id: {send_message["id"]}')
  except HttpError as error:
    print(f"An error occurred: {error}")
    send_message = None
  return send_message

if __name__ == "__main__":
  gmail_send_message()
