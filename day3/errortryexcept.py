import requests

api_key = "93aee1df82c6dd521bf30e4bd14adef3"
city = "Hyderabad"
url = "https://api.openweathermap.org/data/2.5/weather"
params = {"q": city, "appid": api_key, "units": "metric"}

try:
    response = requests.get(url, params=params, timeout=5)
    response.raise_for_status()  # turns 4xx/5xx status codes into exceptions too
    data = response.json()
    print(f"Temperature in {city}: {data['main']['temp']}°C")

except requests.exceptions.Timeout:
    print("Request timed out — server took too long to respond.")
except requests.exceptions.ConnectionError:
    print("Connection failed — check your internet connection.")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")
except requests.exceptions.RequestException as e:
    print(f"Something went wrong: {e}")