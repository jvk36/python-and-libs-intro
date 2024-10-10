import os
from dotenv import load_dotenv
import requests
# from pprint import pprint
from datetime import datetime

# *****************************************************************************
# Register at https://developers.amadeus.com/register to get the keys to 
# access the API
# *****************************************************************************

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
CITY_SEARCH_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_OFFERS_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        load_dotenv()
        self._api_key = os.getenv('AMADEUS_API_KEY')
        self._api_secret = os.getenv('AMADEUS_SECRET')
        self._token = self._get_new_token()

    def _get_new_token(self):
        # Header with content type as per Amadeus documentation
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        # pprint(response.json())
        return response.json()['access_token']

    def get_iata_code(self, city):
        header = {
            "Authorization": "Bearer " + self._token,
        }
        body = {
            "keyword": city,
            "max": 1,
        }
        response = requests.get(url=CITY_SEARCH_ENDPOINT, headers=header, params=body)
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")
            return "Not Found"

        return code

    def get_flight_offers(self, from_city_iata, to_city_iata, date_of_flight: datetime):
        header = {
            "Authorization": "Bearer " + self._token,
        }
        # parameters sample - originLocationCode=LGA&destinationLocationCode=HSV&departureDate=2024-08-03&adults=1&travelClass=ECONOMY&nonStop=false&max=250
        body = {
            "originLocationCode": from_city_iata,
            "destinationLocationCode": to_city_iata,
            "departureDate": date_of_flight.strftime("%Y-%m-%d"),  # "2024-08-03",
            "adults": 1,
            "travelClass": "ECONOMY",
            "nonStop": "false",
            "max": 10,
        }

        response = requests.get(url=FLIGHT_OFFERS_ENDPOINT, headers=header, params=body)
        print(f"Status code {response.status_code}. Flight Offers: {response.text}")
        return response.json()

search = FlightSearch()
print(search.get_iata_code("Huntsville"))
print(search.get_flight_offers("DFW", "LGA", datetime(2024, 10, day=18)))
