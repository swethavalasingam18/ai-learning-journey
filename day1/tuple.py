# Tuple - uses parentheses ()
colors = ("red", "green", "blue")
print(colors)
print(colors[0])       # access works just like a list

# Try to change it - this will cause an error
colors[0] = "yellow"   # TypeError! tuples can't be modified