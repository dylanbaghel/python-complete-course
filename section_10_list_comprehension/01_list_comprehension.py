# List Comprehension

"""
COMPREHENSION:
    --> Comprehensions in Python provide us with a short and concise way to construct new sequences (such as lists, set, dictionary etc.) using sequences which have been already defined. Python supports the following 4 types of comprehensions:
        --> List Comprehensions
        --> Dictionary Comprehensions
        --> Set Comprehensions
        --> Generator Comprehensions
"""

"""
LIST COMPREHENSION:
    --> List comprehension is an elegant way to define and create lists based on existing lists.
    --> [expression(n); for n in list(n)]
    --> We can use conditional(if-else) in comprehension for complex conversion.
    --> Remember, every list comprehension can be rewritten in for loop, but every for loop can’t be rewritten in the form of list comprehension.
"""
names = ['Abhishek', 'Dylan', 'Bittu']

# Make a new list which has surname 'Baghel' with every name in the list names

# Using For Loop
names_with_surname = []
for name in names:
    names_with_surname.append(name + ' Baghel')
print(names_with_surname)

# Python Way - Using Comprehension
names_with_surname2 = [name + ' Baghel' for name in names]
print(names_with_surname)

nums  = [5, 12, 13, 55, 23, 6, 16, 11]
squared_nums = [x*x for x in nums]
print(squared_nums)

"""
Conditional Logic With List Comprehension
    --> If: [x for x in list[] if condition(x)]
    --> If-else [true_exp(x) if conditon(x) else false_exp(x) for x in list[]]
"""

# If in List Comprehension
numbers = list(range(0, 50))
print(numbers)
even_numbers = [n for n in numbers if n % 2 == 0]
print(f"Even: {even_numbers}")
odd_numbers = [n for n in numbers if n % 2 != 0]
print(f"Odd: {odd_numbers}")

# If-else in List Comprehension
mixed = [x*x if x % 2 == 0 else x*x*x for x in nums]
print(mixed)

# Removing Vowels and Creating Capitalize Feature
text = "Programming is the amazing thing in this world!"
text_without_vowels = [char for char in text if char not in "aeiou"]
print("".join(text_without_vowels))

text_capitalize = [f"{char[0].upper()}{char[1:]}" for char in text.split(" ")]
print(" ".join(text_capitalize))