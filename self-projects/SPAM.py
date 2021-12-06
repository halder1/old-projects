import smtplib
import ssl
from time import sleep
import getpass

print("This is an experimental tool that allows you to spam email addresses with the same email. This was made for DEMONSTRATION purposes only.\nYou must edit the message2 variable before running in order to customize the message.")
sleep(1)
sender_email2 = input("Please type the sender email address here and press enter: ")
password2 = input('Type your password and press enter. NOTE that your input is invisible, and it will look like nothing was typed: ')
receiver_email2 = input("Please type the receiver email address here and press enter: ")
subject = input("What is the subject? ")
body = input("Enter body text: ")
sleep(1.25)
print("\nSpamming!")
sleep(1)

while True:
    port2 = 465  # For SSL
    smtp_server2 = "smtp.gmail.com"
    message2 = """
    Subject: """ + subject + """

    """ + body + """ """
    
    #EDIT HERE: SUBJECT OF MESSAGE AND BODY TEXT#

    context2 = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server2, port2, context=context2) as server:
        server.login(sender_email2, password2)
        server.sendmail(sender_email2, receiver_email2, message2)

    
