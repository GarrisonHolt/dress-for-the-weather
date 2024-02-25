import requests
import json
import secrets


class Weather:
    def __init__(self, city: str, temp: float, condition: str) -> None:
        self.city = city
        self.temp = temp
        self.condition = condition

    def get_weather(city):
        URL = f'https://api.weatherapi.com/v1/forecast.json?key={secrets.API_KEY}&q={city}&days=1&aqi=no&alerts=yes'
        request = requests.get(URL)
        if request.status_code == 200:
            data = json.loads(request.text)
            return data
        else:
            print(f"Something went wrong... Status code:{request.status_code}")
            return None

    def generate_dress(data) -> None:
        if data:
            print('Current temperature:', data['current']['temp_f'])
            if data['current']['temp_f'] > 80:
                print('Current temperature is hot... Wear short sleeves.')
            elif 60 <= data['current']['temp_f'] < 80:
                print('Current temperature is cool... Wear long sleeves.')
            else:
                print('Current temperature is cold... Wear long sleeves and a coat.')

            if data['current']['condition']['text'] != 'Sunny':
                print('Not sunny. Might want to bring a rain jacket.')
