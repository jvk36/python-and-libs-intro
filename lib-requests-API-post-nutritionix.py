import os
import requests
from dotenv import load_dotenv


load_dotenv()

# *******************************************************************************
# Setup an account using the free tier at https://developer.nutritionix.com/
# to get the ID and Key.
# *******************************************************************************
NUTRITIONIX_APP_ID = os.environ["NUTRITIONIX_APP_ID"]
NUTRITIONIX_API_KEY = os.environ["NUTRITIONIX_API_KEY"]

HOST_DOMAIN = "https://trackapi.nutritionix.com"
NL_ENDPOINT_OFFSET = "v2/natural/exercise"
NL_ENDPOINT = HOST_DOMAIN + "/" + NL_ENDPOINT_OFFSET

exercises_done = input("Tell me what exercises you did? (Example: walked 40 minutes) - ")
nix_header = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "x-remote-user-id": "0",
}
nix_parameters = {
    "query": exercises_done,
}

response = requests.post(url=NL_ENDPOINT, headers=nix_header, json=nix_parameters)
response.raise_for_status()
print(response.text)
