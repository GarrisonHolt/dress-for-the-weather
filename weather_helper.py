import requests
import json
import secrets
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
    temp_decimal = data['current']['temp_f']
    temp = round(temp_decimal, 0)
    condition = data['current']['condition']['text']
    if temp:
        print('Current temperature:', temp)
        if temp > 75:
            print('Wear short sleeves.')
        elif 60 <= temp < 750:
            print('Wear long sleeves.')
        else:
            print('Wear long sleeves and a coat.')

    if condition != 'Sunny':
        print('Might want to bring a rain jacket too.')

