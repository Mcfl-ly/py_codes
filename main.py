import os
import requests
from dotenv import load_dotenv

load_dotenv()


# AMADEUS
amadeus_api_secret = os.getenv('AMADEUS_API_SECRET')
amadeus_api_key = os.getenv('AMADEUS_API_KEY')
amadeus_token_endpoint = 'https://test.api.amadeus.com/v1/security/oauth2/token'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
body = {'grant_type': 'client_credentials',
        'client_id': amadeus_api_key,
        'client_secret': amadeus_api_secret,}
token_amadeus_getter = requests.post(url=amadeus_token_endpoint, headers=headers, data=body)
amadeus_token = token_amadeus_getter.json()['access_token']

auth_header = {
    "Authorization": f"Bearer {amadeus_token}",

}