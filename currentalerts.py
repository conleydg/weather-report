
import json
import requests

class CurrentAlerts():
    def __init__(self, zipcode):
        self.f = requests.get('http://api.wunderground.com/api/6176857ef9ab82d7/geolookup/alerts/q/{}.json'.format(19352))


    def display(self):
        current_alerts = self.f.json()
        try:
            print(current_alerts['alerts']["type"])
            print(current_alerts['alerts']["description"])
            print(current_alerts['alerts']["expires"])
            print(current_alerts['alerts']["message"])
        except:
            print('There are no alerts currently')
