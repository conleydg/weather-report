
import json
import requests

class CurrentAlerts():
    def __init__(self, zipcode):
        self.f = requests.get('http://api.wunderground.com/api/6176857ef9ab82d7/geolookup/alerts/q/{}.json'.format(19352))
        self.current_alerts = self.f.json()

    def display(self):
        current_alerts = self.current_alerts
        try:
            print('Current Alerts: ', current_alerts['alerts']["type"])
            print('\n','Description\n',  current_alerts['alerts']["description"])
            print('\n', 'Alert Expires: \n', current_alerts['alerts']["expires"])
            print('\n', 'Message: \n', current_alerts['alerts']["message"])
        except:
            print('There are no alerts currently')
