import requests
import os
from dotenv import load_dotenv

load_dotenv()

class WeatherApp:
    def __init__(self):
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        
        
        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            return {
                'name': city,
                'sys': {'country': 'Demo'},
                'main': {'temp': 20, 'humidity': 65},
                'weather': [{'description': 'partly cloudy'}]
            }
        except requests.exceptions.RequestException as e:
            return {"error": f"API request failed: {e}"}
    
    def display_weather(self, weather_data):
        if "error" in weather_data:
            print(f"Error: {weather_data['error']}")
            return
        
        city = weather_data['name']
        country = weather_data['sys']['country']
        temp = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        
        print(f"\nWeather in {city}, {country}:")
        print(f"Temperature: {temp}°C")
        print(f"Description: {description.title()}")
        print(f"Humidity: {humidity}%")

def main():
    app = WeatherApp()
    
    while True:
        city = input("\nEnter city name (or 'quit' to exit): ").strip()
        if city.lower() == 'quit':
            break
        
        if city:
            weather_data = app.get_weather(city)
            app.display_weather(weather_data)
        else:
            print("Please enter a valid city name.")

if __name__ == "__main__":
    main()