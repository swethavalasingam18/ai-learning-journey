import requests

api_key = "93aee1df82c6dd521bf30e4bd14adef3"
city = "Hyderabad"

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}

response = requests.get(url, params=params)
print(response.status_code)
print(response.json())