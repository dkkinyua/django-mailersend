from mailersend import emails
from dotenv import load_dotenv
import os

load_dotenv()

def send_email(email):
    mailer = emails.NewEmail(os.getenv('MAILERSEND_API_KEY'))

    mail_body = {}

    mail_from = {
        "name": "Test Admin",
        "email": "denzo@mailersend.com"
    }

    recipients = [
        {
            "name": "That Guy",
            "email": email, 
        }
    ]

    variables = [
        {
            "email": email,
            "substitutions": [
                {
                    "var": "foo",
                    "value": "bar"
                },
            ]
        }
    ]

    mailer.set_mail_from(mail_from, mail_body)
    mailer.set_mail_to(recipients, mail_body)
    mailer.set_subject("Hello from Adorn.", mail_body)
    mailer.set_template("vywj2lpwx0jg7oqz", mail_body) 
    mailer.set_personalization(variables, mail_body)

    try:
        response = mailer.send(mail_body)
        print("Email sent successfully.", response)
    except Exception as e:
        print(f"Failed to send email: {e}")
