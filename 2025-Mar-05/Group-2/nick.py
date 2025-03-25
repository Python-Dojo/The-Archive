import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

textfile = "./body.txt"

msg = EmailMessage()
msg.set_content("hello")

me =
you =
msg['Subject'] = 'greeting'
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()
