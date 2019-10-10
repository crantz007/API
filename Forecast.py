import requests
from datetime import datetime
import os

def main():
    # ask user to input city and country name
    city_name = input('Enter a city: ')
    country_name = input('Enter a country by 2 letters abbreviation: ')
    # ignore case
    ignore_case_city_name = city_name.lower()
    ignore_case_country_name = country_name.lower()
    # exception
    try:
        # Environment variable key
        key = os.environ.get('WEATHER_KEY')
        query = {'q': f'{ignore_case_city_name},{ignore_case_country_name}', 'units':'imperial', 'appid': key}
        # store
        url = 'https://api.openweathermap.org/data/2.5/forecast'
        # getting data from request
        response = requests.get(url, params=query).json()
        # print forecast with local time which is important for the user
        time = response['list'][0]['dt']
        date = datetime.fromtimestamp(time)
        weather_description = response['list'][0]['weather'][0]['description']
        temp = response['list'][0]['main']['temp']
        wind = response['list'][0]['wind']['speed']
        print(f'The weather @ {date} is {weather_description} with a temp of {temp}F, and a wind speed of {wind}mph.')
    except TypeError as e:
        print(e)
    except KeyError:
        print(response['message'])

if __name__=='__main__':
    main()