# map() Function

"""
map:
    --> A standard function that accepts at least two arguments, a function and "iterable".
"""

# Using Normal Function
names = ["Abhishek", "Dylan", "Bittu"]

def change(name):
    return f"{name} Baghel"

names_with_surname = list(map(change, names))
print(names_with_surname)

# Using Lambda
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda number: number ** 2, numbers))
print(squared_numbers)
