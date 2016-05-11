import json
import requests

class CurrentHurricanes():
    def __init__(self, zipcode):
        self.f = requests.get('http://api.wunderground.com/api/6176857ef9ab82d7/currenthurricane/view.json')


    def display(self):
        current_hurricanes = self.f.json()
        try:
            print(current_hurricanes['currenthurricane']['stormName'])
            print(current_hurricanes['currenthurricane']["current"]["category"])
        except:
            print('There are currently no hurricanes')
