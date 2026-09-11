class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def describe(self):
        print(f"{self.brand}, can go  {self.speed} per hour.")

class Car(Vehicle):              
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)  
        self.doors = doors

    def car_info(self):
        print(f"{self.brand} has {self.doors}")

s = Car("BMW", 40, 85)
s.describe()    #(inherited method)
s.car_info()   # (own method)