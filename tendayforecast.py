import json
import requests


class TenDayForecast():
    def __init__(self, zipcode):
        self.f = requests.get('http://api.wunderground.com/api/6176857ef9ab82d7/geolookup/forecast10day/q/{}.json'.format(19352))

    def display(self):
        ten_day_forecast = self.f.json()
        print(ten_day_forecast['forecast']['simpleforecast'])
