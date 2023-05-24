import json
import requests


#https://countryapi.io/api/all?apikey=


class CountryAPI:
    API_KEY = open('api_key.txt').read()
    BASE_URL = 'https://countryapi.io/api/name'

    def get_countries_by_name(self, country):
        url = f'{self.BASE_URL}/{country}?apikey={self.API_KEY}'
        res = requests.get(url)
        data = res.json()
        keys = list(data.keys())
        return data[keys[0]]


