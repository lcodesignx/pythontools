#!/usr/bin/env python
import requests, json, argparse

def get_forecast(city):
    '''Function to get weather forcast for a city'''

    message = f'Weather forcast for {city}'
    api_key = '74466c79d2480d1529e8ea066fe19b33'
    base_url = 'http://api.weatherstack.com/current?'
    complete_url = base_url + 'access_key=' + api_key + '&query=' + city + '&units=f'

    response = requests.get(complete_url)
    json_obj = response.json()

    location = json_obj["request"]["query"]
    weather_descriptions = json_obj["current"]["weather_descriptions"][0] 
    temperature = json_obj["current"]["temperature"]
    chance_of_rain = json_obj["current"]["precip"]

    print(
       f'{location}\n'
       f'It is currently {weather_descriptions}'
       f' with a temperature of {temperature} degrees'
       f' and {chance_of_rain}% chance of rain'
    )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get city weather forecast')
    parser.add_argument('city', help='City to get weather forecast for')
    args = parser.parse_args()

    get_forecast(args.city)
