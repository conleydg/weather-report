import json
import requests
import re

from currentalerts import CurrentAlerts
from currentconditions import CurrentConditions
from currenthurricanes  import CurrentHurricanes
from sunrisesunset import SunriseSunset
from tendayforecast import TenDayForecast

def get_zipcode():
    print('Please enter the five digit zip code to check the weather')
    while True:
        zip_code = input(': ')
        if re.match('^\d{5}$', zip_code):
            return zip_code
        else:
            print("Please enter a five digit zip code")

def store_preference():
    print('Would you like to store your data?')
    while True:
        yes_no = input('y/N: ' )
        if yes_no == 'y':
            return True
        else:
            return False


def new_request():
    print('Would you like to run new requests(or use stored data?)')
    while True:
        yes_no = input('y/N: ')
        if yes_no == 'y':
            return True
        elif yes_no =='n':
            return False


def make_requests(zip_code):
    current_alerts = CurrentAlerts(zip_code)
    current_conditions = CurrentConditions(zip_code)
    current_hurricanes = CurrentHurricanes(zip_code)
    sunrise_sunset = SunriseSunset(zip_code)
    ten_day_forecast = TenDayForecast(zip_code)
    return current_alerts, current_conditions, current_hurricanes, sunrise_sunset, ten_day_forecast


def store_endpoints(current_alerts, current_conditions, current_hurricanes, sunrise_sunset, ten_day_forecast):
    with open('currentalerts.txt', 'w') as outfile:
        json.dump(current_alerts, outfile)
    with open('currentconditions.txt', 'w') as outfile:
        json.dump(current_conditions, outfile)
    with open('currenthurricanes.txt', 'w') as outfile:
        json.dump(current_hurricanes, outfile)
    with open('sunrisesunset.txt', 'w') as outfile:
        json.dump(sunrise_sunset, outfile)
    with open('tendayforecast.txt', 'w') as outfile:
        json.dump(ten_day_forecast, outfile)


def open_stored_endpoints():
    with open('currentalerts.txt') as data_file:
        current_alerts = json.load(data_file)
    with open('currentconditions.txt') as data_file:
        current_conditions = json.load(data_file)
    with open('currenthurricanes.txt') as data_file:
        current_hurricanes = json.load(data_file)
    with open('sunrisesunset.txt') as data_file:
        sunrisesunset= json.load(data_file)
    with open('tendayforecast.txt') as data_file:
        ten_day_forecast = json.load(data_file)
    return(current_alerts, current_conditions, current_hurricanes,
                        sunrise_sunset, ten_day_forecast)


def main():
    zip_code = get_zipcode()
    current_alerts, current_conditions, current_hurricanes, sunrise_sunset, ten_day_forecast = make_requests(zip_code)
    current_alerts.display()
    current_conditions.display()
    current_hurricanes.display()
    sunrise_sunset.display()
    ten_day_forecast.display()




if __name__ == '__main__':
    main()
