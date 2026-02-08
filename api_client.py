import requests

API_KEY = "5f0c7d277265735d5363872dddf4e57a"  # <-- Paste your OpenWeather key here
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"❌ API Error for {city}: {e}")
        return None


if __name__ == "__main__":
    test_city = "Mumbai"
    data = fetch_weather(test_city)

    if data:
        print("✅ Weather data fetched successfully!")
        print(data)
    else:
        print("❌ Failed to fetch weather data")
