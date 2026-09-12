import requests
#https://api.github.com/search/repositories?q=language:python+stars:>10000
response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "language:python stars:>10000"}
)
data = response.json()
print(data["total_count"])
for repo in data["items"][:5]:
    print(repo["full_name"], "-", repo["stargazers_count"] ,"-" , repo["name"])