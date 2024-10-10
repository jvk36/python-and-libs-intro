import requests
import os
from dotenv import load_dotenv


load_dotenv()

# *** STEP 1 - Create Account

# *******************************************************************************
# With the Pixela API service, you can get a GitHub like graph that expresses 
# the degree of your daily various activities on a basis with a vivid 
# gradation. All operations are performed by API. 
# Step 1: Create Account
# Step 2: Create Graph
# Step 3: Post Activity
#
# NOTE: One could also delete and update pixels in an existing graph.
#
# The graph is accessible at the URL: 
# https://pixe.la/v1/users/johnkonnayilvincent/graphs/<GRAPH ID>.html 
#
# Created Account Profile at https://pixe.la/@<USERNAME>
# 
# *******************************************************************************
PIXELA_USER_NAME = os.environ["PIXELA_USER_NAME"]
PIXELA_TOKEN = os.environ["PIXELA_TOKEN"]

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)
