import secrets
import requests
import json

URL = f"https://ipgeolocation.abstractapi.com/v1?api_key={secrets.IP_API_KEY}"


def get_current_city():
    response = requests.get(URL)
    data = response.json()
    if response.status_code == 200:
        print(f"City name {data['city']}")
        return data["city"]
