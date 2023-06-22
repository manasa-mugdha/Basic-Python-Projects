'''
Features:
User can enter a city or zip code to get the weather forecast.
The program fetches weather data from a weather API.
The program displays the current weather information including temperature, humidity, wind speed, and weather conditions.
The program presents a forecast for the upcoming days.

'''

#code

import requests

def fetch_weather_data(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def display_weather_data(weather_data):
    if weather_data["cod"] == "404":
        print("Location not found.")
        return

    print(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    print(f"Weather Conditions: {weather_data['weather'][0]['description']}")

def main():
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    location = input("Enter a city or zip code: ")
    weather_data = fetch_weather_data(api_key, location)
    display_weather_data(weather_data)

if __name__ == '__main__':
    main()
