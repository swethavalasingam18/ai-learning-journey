import requests

api_key = "93aee1df82c6dd521bf30e4bd14adef3"
city = "Hyderabad"

url = "https://api.openweathermap.org/data/2.5/weather"
params = {"q": city, "appid": api_key, "units": "metric"}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(f"Temperature in {city}: {data['main']['temp']}°C")
elif response.status_code == 401:
    print("Authentication failed — check your API key, or it may still be activating.")
elif response.status_code == 404:
    print("City not found — check the spelling.")
else:
    print(f"Unexpected error: {response.status_code}")
    print(response.json())