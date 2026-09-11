class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"I'm {self.name}, {self.age} years old.")

class Student(Person):              # Student inherits from Person
    def __init__(self, name, age, score):
        super().__init__(name, age)  # calls Person's __init__
        self.score = score

    def show_score(self):
        print(f"{self.name} scored {self.score}")

s = Student("Swetha", 40, 85)
s.introduce()    # I'm Swetha, 40 years old.  (inherited method)
s.show_score()   # Swetha scored 85           (own method)