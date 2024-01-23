import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change this to "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']

            return f"Weather in {city}: {weather_description}, Temperature: {temperature}°C, Humidity: {humidity}%"
        else:
            return f"Error: {data['message']}"

    except Exception as e:
        return f"An error occurred: {e}"

# Replace 'your_api_key' with your actual OpenWeatherMap API key
api_key = '0b788c6011f6b4523f5c1b09ed0fe137'
city = 'New York'

result = get_weather(api_key, city)
print(result)
