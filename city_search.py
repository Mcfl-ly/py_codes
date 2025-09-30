import requests
from main import auth_header


# response = requests.get("https://test.api.amadeus.com/v1/reference-data/locations/cities?countryCode=FR&keyword=PARIS&max=1", headers=auth_header)


class CitySearch:
    def __init__(self):


        self.sheety_endpoint = "https://api.sheety.co/9fd8cbe7d318da234e51ee49e023f971/voos/prices"
        self.city_search_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        self.auth_header = auth_header
        self.low_price = 4000

    def add_sheety(self, add_country, add_city):
        add_params = {
            "countryCode": add_country.upper(),
            "keyword": add_city.upper(),
            "max": 1,
        }
        response_city_search = requests.get(self.city_search_endpoint, headers=self.auth_header, params=add_params)
        iata_code = response_city_search.json()['data'][0]['iataCode']
        city = response_city_search.json()['data'][0]['name']

        #PARAMETROS DA PLANILHA
        sheety_params = {
            "price": {
                "city": city,
                "iataCode": iata_code,
                "lowestPrice": self.low_price,
            }
        }
        response_sheety = requests.post(self.sheety_endpoint, json=sheety_params)

    def origin_city(self, country, city):
        origin_params = {
            "countryCode": country.upper(),
            "keyword": city.upper(),
            "max": 1,
        }
        response_origin = requests.get(self.city_search_endpoint, headers=self.auth_header, params=origin_params)
        origin_iata_code = response_origin.json()['data'][0]['iataCode']
        return origin_iata_code

