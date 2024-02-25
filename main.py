import weather_helper
import geo_helper
if __name__ == '__main__':

    def run_app():
        user_choice = input("Would you like to use your current location based on IP Address (Y/N)").lower()

        if user_choice == "y":
            city = geo_helper.get_current_city()
        elif user_choice == "n":
            city = input('Enter city name: ')
        else:
            city = input('Enter city name: ')
        weather_data = weather_helper.Weather.get_weather(city)
        weather_helper.Weather.generate_dress(weather_data)

    run_app()