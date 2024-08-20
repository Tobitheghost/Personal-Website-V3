# from email_validator import validate_email, EmailNotValidError
from flask_mail import Message
from smtplib import SMTPAuthenticationError
from .paths.utils.secret import mail_username
from main import mail
import logging

logger = logging.getLogger(__name__)

def check_email(name, textarea, email, test):
    print("checking...")
    try:
        if validate_email(email, check_deliverability=True):
            print("validating...")
            if int(test) == 6:
                print("mathing...")
                incoming_msg = Message(
                    subject=f"Contact Webpage:: {name} at {email}",
                    body=textarea,
                    recipients=[mail_username],
                    sender=email
                    )

                outgoing_msg = Message(
                    subject="Thank You for Contacting Me!",
                    body="Thank you for getting in contact with me. I will read your message asap!",
                    recipients=[email],
                    sender=mail_username
                    )
                try:
                    mail.send(incoming_msg)
                    mail.send(outgoing_msg)
                    response = "Email Sent!", "succsess"
                except SMTPAuthenticationError:
                    response = "SMTP Server Error: Please send an email through your personal inbox while Tobi fixes this", "error"
                    print(SMTPAuthenticationError)
                    resonse_log = {
                        "response": [response, "535, b'5.7.8 Username and Password not accepted. For more information, go to 5.7.8 \
                        https://support.google.com/mail/?p=BadCredentials b17-20020a0c9b11000000b00690494d2766sm4167396qve.96 - gsmtp"],
                        "name": name,
                        "email_msg": textarea,
                        "email": email,}
                    logger.error(resonse_log)
                    # Log (535, b'5.7.8 Username and Password not accepted. For more information, go to\n5.7.8  
                    # https://support.google.com/mail/?p=BadCredentials b17-20020a0c9b11000000b00690494d2766sm4167396qve.96 - gsmtp')

            else:
                print("math wrong")
                response = "Incorrect Answer" ,"error"
        else:
            print("email wrong")
            response = "Invalid Email" ,"error"
    except EmailNotValidError as e:
        print(e)
        response = e ,"error"
    return response

