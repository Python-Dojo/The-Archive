from smtplib import SMTP
import ssl
from email.message import EmailMessage

print(
    """
 _____                         _____                _ _   _____                _
/  ___|                       |  ___|              (_) | /  ___|              | |
\ `--. _   _ _ __   ___ _ __  | |__ _ __ ___   __ _ _| | \ `--.  ___ _ __   __| | ___ _ __
 `--. \ | | | '_ \ / _ \ '__| |  __| '_ ` _ \ / _` | | |  `--. \/ _ \ '_ \ / _` |/ _ \ '__|
/\__/ / |_| | |_) |  __/ |    | |__| | | | | | (_| | | | /\__/ /  __/ | | | (_| |  __/ |
\____/ \__,_| .__/ \___|_|    \____/_| |_| |_|\__,_|_|_| \____/ \___|_| |_|\__,_|\___|_|
            | |
            |_|
"""
)


print("Trying to send emails…")

sender_email =
sender_password =
app_password =

context = ssl.create_default_context()
server = "smtp.gmail.com"
port = 587

helen =
jonathan =
nick =
ray =
recipients = [
    # helen,
    jonathan,
    nick,
    ray
]

content = """
Finland is the happiest country on Earth. According to the
World Happiness Report, it has been for six years in a row.
It’s not really surprising, given that Finland is the home
of Santa Claus, reindeer and one sauna for every 1.59
people.
"""

with SMTP(server, port) as smtp:
    # for recipient in recipients:
    #     print(f"Sending email to {recipient}")
    msg = EmailMessage()
    msg.set_content(content)
    msg["Subject"] = "Hello from Python Dojo"
    msg["From"] = sender_email
    msg["To"] = ",".join(recipients)

    smtp.ehlo() # apparently this is optional
    smtp.starttls(context=context)
    smtp.ehlo()
    smtp.login(sender_email, app_password)
    smtp.send_message(msg)
