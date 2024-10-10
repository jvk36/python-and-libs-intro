import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv


load_dotenv()


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")   
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")  

# *******************************************************************************
# Setup an account at https://openweathermap.org/
# to get the Key.
# *******************************************************************************
OWM_ENDPOINT = os.environ.get("OWM_ENDPOINT")  
OWM_API_KEY = os.environ.get("OWM_API_KEY")   

weather_params = {
    "lat": 40.94,
    "lon": -73.11,
    "appid": OWM_API_KEY,
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT, weather_params)
response.raise_for_status()
# print(response)
data = response.json()
# print(data)

# data = {'cod': '200', 'message': 0, 'cnt': 4, 'list': [{'dt': 1720623600, 'main': {'temp': 298.58, 'feels_like': 299.53, 'temp_min': 298.58, 'temp_max': 300.24, 'pressure': 1013, 'sea_level': 1013, 'grnd_level': 1011, 'humidity': 90, 'temp_kf': -1.66}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 100}, 'wind': {'speed': 5.29, 'deg': 203, 'gust': 8.46}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-10 15:00:00'}, {'dt': 1720634400, 'main': {'temp': 299.12, 'feels_like': 299.12, 'temp_min': 299.12, 'temp_max': 300.21, 'pressure': 1013, 'sea_level': 1013, 'grnd_level': 1011, 'humidity': 85, 'temp_kf': -1.09}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 99}, 'wind': {'speed': 7.06, 'deg': 192, 'gust': 10.98}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-10 18:00:00'}, {'dt': 1720645200, 'main': {'temp': 299.18, 'feels_like': 299.18, 'temp_min': 299.18, 'temp_max': 299.48, 'pressure': 1012, 'sea_level': 1012, 'grnd_level': 1010, 'humidity': 82, 'temp_kf': -0.3}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 100}, 'wind': {'speed': 9.11, 'deg': 188, 'gust': 14.37}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-10 21:00:00'}, {'dt': 1720656000, 'main': {'temp': 297.64, 'feels_like': 298.34, 'temp_min': 297.64, 'temp_max': 297.64, 'pressure': 1010, 'sea_level': 1010, 'grnd_level': 1009, 'humidity': 84, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 90}, 'wind': {'speed': 9.02, 'deg': 186, 'gust': 15.78}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-11 00:00:00'}], 'city': {'id': 5116060, 'name': 'East Setauket', 'coord': {'lat': 40.94, 'lon': -73.11}, 'country': 'US', 'population': 17006, 'timezone': -14400, 'sunrise': 1720603791, 'sunset': 1720657529}}
# print(data["list"][0]["weather"][0]["id"])
weather_ids = [data["list"][i]["weather"][0]["id"] for i in range(4)]
# print(weather_ids)
if len([w_id for w_id in weather_ids if w_id < 700]):
    message = "It is going to rain today. Remember to bring an ☂️."
else:
    message = "No rain"

print(message)
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

message = client.messages.create(
    body=message,
    from_="whatsapp:+14155238886",  # for SMS - need extra verification - +18882314251",
    to="whatsapp:+17162819655",
)

print(message.status)

