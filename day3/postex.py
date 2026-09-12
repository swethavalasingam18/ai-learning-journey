import requests
data_to_send ={"name " : "Swetha" , "age" : 40 , "role" : "AI Engineer"}
response = requests.post("https://httpbin.org/post" , json=data_to_send)

print(response.status_code)
print(response.json())