import os
import requests
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

# *******************************************************************************
# Setup an account using the free tier at https://dashboard.sheety.co/ 
#  through "Sign In With Google". The Google Sheets in that
# account can then be hooked up for sheety API access by creating a new project
# and pasting the sheet URL in.
# 
# Each project provides an endpoint and bearer token which can be used to use
# the API to manipulate Google Sheets!
# *******************************************************************************
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]

sheety_header = {
    "Authorization": SHEETY_TOKEN,
}

today = datetime.now()

sheety_body = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),  # "DD/MM/YYYY",
        "time": today.strftime("%H:%M:%S"),  # "15:00:00",
        "exercise": "Walking",
        "duration": "40",
        "calories": "170",
    }
}
# print(sheety_body)

response = requests.post(url=SHEETY_ENDPOINT, json=sheety_body, headers=sheety_header)
response.raise_for_status()
print(response.text)
print(response.json())
