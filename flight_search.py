import requests
from city_search import CitySearch
from main import auth_header

ORIGIN_COUNTRY = 'br'
ORIGIN_CITY = 'sao paulo'

class FlightSearch:
    def __init__(self, city_search: CitySearch):
        self.iata_codes = []
        self.values_sheety = requests.get('https://api.sheety.co/9fd8cbe7d318da234e51ee49e023f971/voos/prices')
        for i in self.values_sheety.json()['prices']:
            # print(i['iataCode'])
            self.iata_codes.append(i['iataCode'])


        self.auth_header = auth_header
        self.city_search = city_search
        self.origin_iata = city_search.origin_city(ORIGIN_COUNTRY,ORIGIN_CITY)
        self.flight_offer_endpoint = 'https://test.api.amadeus.com/v2/shopping/flight-offers'

        for i in self.iata_codes:
            self.destiny_iata = i

            self.flight_offer_params = {
                "originLocationCode": self.origin_iata,
                "destinationLocationCode": self.destiny_iata,
                "departureDate": '2025-10-11',
                "adults": 1,
                "currencyCode": "BRL",
                "max": 1,
            }

    def find_flights(self):
        response = requests.get(self.flight_offer_endpoint, headers=self.auth_header, params=self.flight_offer_params)
        print(response.json())

cs = CitySearch()
fs = FlightSearch(cs)
fs.find_flights()

