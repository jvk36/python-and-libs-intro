from datetime import datetime
import requests
import os
from dotenv import load_dotenv


load_dotenv()

# *** STEP 3 - Post Activity

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
GRAPH_ID = "graph1"

graph_endpoint = f"{pixela_endpoint}/{PIXELA_USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# today = datetime(2024, 7, 9)

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10",
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

response = requests.post(url=graph_endpoint, json=pixel_config, headers=headers)
print(response.text)

# graph is at https://pixe.la/v1/users/johnkonnayilvincent/graphs/graph1.html
