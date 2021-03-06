import json
import requests

class SunriseSunset():
    def __init__(self, zipcode):
        self.f = requests.get('http://api.wunderground.com/api/6176857ef9ab82d7/geolookup/astronomy/q/{}.json'.format(19352))


    def display(self):
        sunrise_sunset = self.f.json()
        print('Sunrise- ', sunrise_sunset['moon_phase']['sunrise']['hour'], ':', sunrise_sunset['moon_phase']['sunrise']['minute'])
        print('Sunset- ', sunrise_sunset['moon_phase']['sunset']['hour'], ':', sunrise_sunset['moon_phase']['sunset']['minute'])
