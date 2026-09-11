def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8

def get_name_and_age():
    name = "Swetha"
    age = 40
    return name, age

n, a = get_name_and_age()
print(n)  # Swetha
print(a)  # 40

result = get_name_and_age()
print(result)      # ('Swetha', 40)
print(result[0])   # Swetha
print(result[1])   # 40
def greet(name):
    print(f"Hello, {name}")
    # no return statement

x = greet("Swetha")   # prints "Hello, Swetha"
print(x)               # None
def check_age(age):
    if age < 0:
        return "Invalid age"
    return f"Age is {age}"

print(check_age(-5))   # Invalid age
print(check_age(30))   # Age is 30


def devide(num1,num2):
    if num2 != 0:
          result= num1 / num2
          return result
    else:
        return f"{num2} is zero we cant devide"

    
print(devide(42,21))
print(devide(23,0))



