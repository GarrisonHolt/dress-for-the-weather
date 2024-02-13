import weather_helper

if __name__ == '__main__':
    weather_data = weather_helper.get_weather()
    weather_helper.generate_dress(weather_data)