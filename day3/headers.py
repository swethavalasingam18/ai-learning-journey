import requests

data_to_send = {"name": "Swetha", "age": 40, "role": "AI Engineer"}

my_headers = {
    "User-Agent": "swetha-learning-app",
    "X-Custom-Note": "day3-practice"
}

response = requests.post(
    "https://httpbin.org/post",
    json=data_to_send,
    headers=my_headers
)

print(response.status_code)
print(response.json())