def greet(name):
    return f"hello ,{name}"
print(greet("swetha"))

def greettwo(name , greeting="hello"):
    return f"{greeting} , {name}"
print(greettwo("swetha"))
print("welcome!" , "swetha")

def describe_pet(name , age, breed):
    return f"{name}  {age} years old {breed} dog"
print(describe_pet(age=3 , name="bruno" ,breed="german shepard"))


def add_allnumbers(*arr):
    return sum(arr)
print(add_allnumbers(22,49,57,65,89))    #282




def print_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_info(name="swetha", age=40, location="hyderabad", role="AI Engineer")