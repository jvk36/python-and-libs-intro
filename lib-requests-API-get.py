import requests


response = requests.get("http://api.open-notify.org/iss-now.json")
# print(response)
data = response.json()
print(type(data))
print(data["iss_position"])
