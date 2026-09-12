import requests
# get data from site and print 5 digfferent jokes

#Use the free public API https://api.punkapi.com won't work anymore (deprecated) — 
# instead use https://catfact.ninja/fact or 
# https://official-joke-api.appspot.com/random_joke:


for i in range(5):
 response = requests.get(
    "https://official-joke-api.appspot.com/random_joke"
)
data = response.json()
print(data["setup"], "-" , data["punchline"])