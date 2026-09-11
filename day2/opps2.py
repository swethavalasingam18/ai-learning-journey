class Student:
    school = "AI Academy"   # class attribute — shared by ALL instances

    def __init__(self, name):
        self.name = name    # instance attribute — unique to each object

s1 = Student("Swetha")
s2 = Student("Ravi")

print(s1.school)  # AI Academy
print(s2.school)  # AI Academy
print(s1.name)    # Swetha
print(s2.name)    # Ravi