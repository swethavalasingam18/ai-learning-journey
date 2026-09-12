import requests
response = requests.get("https://api.github.com/users/octocat")
#print(response.status_code)
#print(response.json()) 
data=response.json()
print(data["user_view_type"])
print(data["created_at"])
