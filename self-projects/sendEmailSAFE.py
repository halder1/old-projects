import smtplib
import ssl
from time import sleep

print("This is an experimental tool that allows you to send emails. NOTE: You must edit the message2 variable before running in order to customize your email subject & body text.")
sleep(1)
sender_email2 = input("Please type the sender email address here and press enter: ")
password2 = input("Please type the password of the designated sender email here and press enter: ")
receiver_email2 = input("Please type the receiver email address here and press enter: ")
sleep(1.25)
print("\Sending!")
sleep(1)

port2 = 465  # For SSL
smtp_server2 = "smtp.gmail.com"
message2 = """  
Subject: (subject goes here)

(body text goes here)."""

#EDIT HERE: SUBJECT OF MESSAGE AND BODY TEXT#

context2 = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server2, port2, context=context2) as server:
    server.login(sender_email2, password2)
    server.sendmail(sender_email2, receiver_email2, message2)


