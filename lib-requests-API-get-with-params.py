import requests
from datetime import datetime


MY_LAT=40.941429
MY_LONG=-73.106003

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# print(response)
data = response.json()
# print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
sunrise_time = sunrise.split("T")[1]
print(f"Sunrise at (lat, lng) ({MY_LAT}, {MY_LONG} is at {sunrise_time}.")
# sunrise_hour = int(sunrise_time.split(":")[0])
# print(sunrise_hour)
now = str(datetime.now())
# now_time = now.split(" ")[1]
# now_hour = int(now_time.split(":")[0])
print(f"Current Time: {now}")
# print(now_hour)
