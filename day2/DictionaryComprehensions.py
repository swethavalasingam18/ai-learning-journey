words = ["python", "is", "fun"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)  # {'python': 6, 'is': 2, 'fun': 3}

numbers = [1, 2, 3, 4, 5, 6]
squares_of_evens = {n: n * n for n in numbers if n % 2 == 0}
print(squares_of_evens)  # {2: 4, 4: 16, 6: 36}

prices = {"apple": 100, "banana": 40, "mango": 150}

# add 10% tax to every price
prices_with_tax = {item: price * 1.1 for item, price in prices.items()}
print(prices_with_tax)
# {'apple': 110.00000000000001, 'banana': 44.0, 'mango': 165.00000000000003}

original = {"a": 1, "b": 2, "c": 3}
swapped = {value: key for key, value in original.items()}
print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}

students = {"Swetha": 85, "Ravi": 92, "Kiran": 78}
passed ={student: marks for student, marks in students.items() if marks > 80}
print(passed)
grade ={
     student: ( "A" if marks >= 90  else ("B" if marks >=80  else "C"))
           for student,marks in students.items()}
print(grade)
