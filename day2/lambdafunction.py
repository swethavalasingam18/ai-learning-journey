square = lambda x: x * x
print(square(5))  # 25
add = lambda a, b: a + b
print(add(3, 4))  # 7
people = [("Swetha", 40), ("Ravi", 25), ("Kiran", 35)]

# sort by age (the second item in each tuple)
sorted_people = sorted(people, key=lambda person: person[1])
print(sorted_people)
# [('Ravi', 25), ('Kiran', 35), ('Swetha', 40)]


numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, numbers))
print(squared)  # [1, 4, 9, 16]


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8]


students = [
    {"name": "Swetha", "score": 85},
    {"name": "Ravi", "score": 92},
    {"name": "Kiran", "score": 78}
]


# Task 1: sort by score, highest first
sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
print(sorted_students)

# Task 2: only students who scored above 80
high_scorers = list(filter(lambda x: x["score"] > 80, students))
print(high_scorers)