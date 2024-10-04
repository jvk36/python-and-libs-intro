import smtplib
import os
from dotenv import load_dotenv


load_dotenv()

SMTP_ADDRESS = os.environ["SMTP_ADDRESS"]
SMTP_PORT = int(os.environ["SMTP_PORT"])
EMAIL_ADDRESS = os.environ["EMAIL_ADDRESS"]
# the app password needs to be set under your google account and pasted here.
# to set it, sign-in after enabling 2-step verification and click on App Password -
# Google might be moving away from this as there is a note that says to use
# "sign in with google" instead of App passwords
APP_PASSWORD = os.environ["APP_PASSWORD"]

with smtplib.SMTP(SMTP_ADDRESS, SMTP_PORT) as connection:
    connection.starttls()
    connection.login(user=EMAIL_ADDRESS, password=APP_PASSWORD)
    connection.sendmail(from_addr=EMAIL_ADDRESS,
                        to_addrs="JohnKonnayilVincent@gmail.com",
                        msg=f"Subject: Test Message Subject!\n\nTest Message Body!".encode("utf-8"))
