person= {
    "name": "swetha",
    "age": 40,
    "city": "Hyderabad",
    "is_working": False
}

print(person)
print(person["name"])   #access value by key
print(person["age"])

#add new key value
person["skills"] =["php","python","n8n"]
print(person)

#update existing value 
person["is_working"] =True
print(person)


#loop through all keys and values
for key, value in person.items():
    print(key,":" ,value)