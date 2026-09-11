class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def display(self):
        print(f"{self.name}, Age: {self.age}, Score: {self.score}")

s1 = Student("Swetha", 40, 85)
s1.display()   # Swetha, Age: 40, Score: 85