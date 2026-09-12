numbers = [10, 20, 30, 40]
count =len(numbers)
total = 0
for num in numbers:
    total = total + num   # add each number to the running total

average = total/count             # hint: total divided by how many numbers there are

print("Sum:", total)
print("Average:", average)