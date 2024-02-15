import weather_helper

if __name__ == '__main__':
    city = input('Enter your city: ').lower()
    weather_data = weather_helper.get_weather(city)
    weather_helper.generate_dress(weather_data)