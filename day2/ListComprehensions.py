numbers=[1,2,3,4,5]
squared = [n * n for n in numbers]
print(squared)  # [1, 4, 9, 16, 25]

firnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in firnumbers if n % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

secnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_evens = [n * n for n in secnumbers if n % 2 == 0]
print(squared_evens)  # [4, 16, 36, 64, 100]

names = ["swetha", "ravi", "kiran"]
capitalized = [name.upper() for name in names]
print(capitalized)  # ['SWETHA', 'RAVI', 'KIRAN']

thinumbers = [1, 2, 3, 4, 5]
labels = ["even" if n % 2 == 0 else "odd" for n in thinumbers]
print(labels)  # ['odd', 'even', 'odd', 'even', 'odd']


words = ["python", "is", "fun", "and", "powerful"]
eachwordlen =[len(word) for word in words]
print(eachwordlen)
longword =[word for word in words if len(word) > 3]
print(longword)
