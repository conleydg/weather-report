import json
import requests


class TenDayForecast():
    def __init__(self, zipcode):
        self.f = requests.get('http://api.wunderground.com/api/6176857ef9ab82d7/geolookup/forecast10day/q/{}.json'.format(19352))

    def display(self):
        ten_day_forecast = self.f.json()
        ten_day_forecast = ten_day_forecast['forecast']['txt_forecast']['forecastday']
        for day_forecast in ten_day_forecast:
            day= day_forecast['title']
            weather= day_forecast['fcttext']
            print(day, '\n', weather, '\n')
