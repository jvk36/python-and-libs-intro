import os
from dotenv import load_dotenv


load_dotenv()

SMTP_ADDRESS = os.environ["SMTP_ADDRESS"]
SMTP_PORT = int(os.environ["SMTP_PORT"])
EMAIL_ADDRESS = os.environ["EMAIL_ADDRESS"]

print(f"SMTP_ADDRESS: {SMTP_ADDRESS}")
print(f"SMTP_PORT: {SMTP_PORT}")
print(f"EMAIL_ADDRESS: {EMAIL_ADDRESS}")
