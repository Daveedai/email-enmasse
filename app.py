import csv, smtplib, ssl
from decouple import config

message = """Subject: Test
    
This message is sent to you, {name}, from Python."""

port = 465 # For SSL
smtp_server = "smtp.gmail.com"
SENDER = config('user', default='')
password = config('password', default='')


# Create a secure SSL context
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(SENDER, password)
    with open("contacts.csv") as file:
        pass