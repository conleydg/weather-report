import json
import requests

class CurrentConditions():
    def __init__(self, zipcode):
        self.f = requests.get('http://api.wunderground.com/api/6176857ef9ab82d7/geolookup/conditions/q/{}.json'.format(19352))


    def display(self):
        current_conditions = self.f.json()
        print(current_conditions['current_observation']['weather'])
        print(current_conditions['current_observation']["temp_f"])
        print(current_conditions['current_observation']["relative_humidity"])
        print(current_conditions['current_observation']["wind_string"])
        print(current_conditions['current_observation']['feelslike_f'])
