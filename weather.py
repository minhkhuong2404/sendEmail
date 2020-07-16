import json
import sys

import requests
from datetime import datetime
import os.path
from os import path


# find the city id in the city.list.json

def call_weather():
    location = 1566083  # change your city id
    api_key = "8280a40d0337be4dedf078ccb4058eb4"
    with open('city.list.json', 'r') as f:
        listOfCity = json.load(f)

    lon = 0
    lat = 0
    city = ""
    country = ""
    for cityId in listOfCity:
        if cityId['id'] == location:
            lon = cityId['coord']['lon']
            lat = cityId['coord']['lat']
            city = cityId['name']
            country = cityId['country']

    url = 'https://api.openweathermap.org/data/2.5/onecall?lat=' + str(lat) + '&lon=' + str(
        lon) + '&exclude=hourly&appid=' + api_key + '&units=metric'
    response = requests.get(url)
    response.raise_for_status()

    weatherDaily = json.loads(response.text)
    wd = weatherDaily["daily"]
    now = weatherDaily["current"]
    UTC7 = 3600 * 7

    # file = open("/Users/minhkhuonglu/Desktop/Pycharm/weatherForecast/weather.txt", "w")
    # file.write("Weather forecast")
    # file.close()
    sys.stdout = open('weather.txt', 'w')
    print("Getting the weather in: " + city + ", " + country)
    print("Current weather\n")
    print("Request at: " + datetime.utcfromtimestamp(now['dt'] + UTC7).strftime('%Y-%m-%d %H:%M:%S'))
    print("Today: " + now['weather'][0]['main'] + " - " + now['weather'][0]['description'])
    print("Temp: " + str(now['temp']))
    print("Humid: " + str(now['humidity']) + " %\n")
    print("Feel like: " + str(now['feels_like']))
    print("Wind_speed: " + str(now['wind_deg']) + " m/s\n")
    sun_rise = now['sunrise'] + UTC7
    sun_set = now['sunset'] + UTC7
    sun_rise_format = datetime.utcfromtimestamp(sun_rise).strftime('%Y-%m-%d %H:%M:%S')
    sun_set_format = datetime.utcfromtimestamp(sun_set).strftime('%Y-%m-%d %H:%M:%S')
    print("Sun rise at: " + sun_rise_format)
    print("Sun set at: " + sun_set_format)
    print("Cloud: " + str(now['clouds']) + " %")
    print("UV index: " + str(now['uvi']))
    try:
        print("Rain: " + str(now['rain']) + " mm")
    except KeyError:
        print("No rain")
    print("====================================\n")
    print("Forecast for the next 7 days\n")

    for i in range(1, 8):
        print("\nDay " + str(i) + ": " + datetime.utcfromtimestamp(wd[i]['dt'] + UTC7).strftime('%Y-%m-%d'))
        print("Request at: " + datetime.utcfromtimestamp(wd[i]['dt'] + UTC7).strftime('%Y-%m-%d %H:%M:%S'))
        print("Today: " + wd[i]['weather'][0]['main'] + " - " + wd[i]['weather'][0]['description'])
        print("Temp from " + str(wd[i]['temp']['min']) + " to " + str(wd[i]['temp']['max']))
        print("Feel like")
        print("at day: " + str(wd[i]['feels_like']['day']))
        print("at night: " + str(wd[i]['feels_like']['night']))
        print("at evening: " + str(wd[i]['feels_like']['eve']))
        print("at morning: " + str(wd[i]['feels_like']['morn']))
        print("Humid: " + str(wd[i]['humidity']) + " %")
        print("Wind_speed: " + str(wd[i]['wind_deg']) + " m/s")
        sun_rise = wd[i]['sunrise'] + UTC7
        sun_set = wd[i]['sunset'] + UTC7
        sun_rise_format = datetime.utcfromtimestamp(sun_rise).strftime('%Y-%m-%d %H:%M:%S')
        sun_set_format = datetime.utcfromtimestamp(sun_set).strftime('%Y-%m-%d %H:%M:%S')

        print("Sun rise at: " + sun_rise_format)
        print("Sun set at: " + sun_set_format)
        print("Cloud: " + str(wd[i]['clouds']) + " %")
        print("UV index: " + str(wd[i]['uvi']))
        try:
            print("Rain: " + str(now['rain']) + " mm")
        except KeyError:
            print("No rain")
        print("=============================================")
    sys.stdout.close()


if __name__ == '__main__':
    call_weather()
