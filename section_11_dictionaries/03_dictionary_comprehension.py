# Dictionary Comprehension

"""
DICTIONARY COMPREHENSION:
    --> Like List Comprehension, Python allows dictionary comprehensions. We can create dictionaries using simple expressions.
"""

numbers = dict(first=1, second=2, third=3)
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
print(squared_numbers)

str1 = 'ABC'
str2 = '123'
combo = {str1[i]:str2[i] for i in range(0, len(str1))}
print(combo)

person = dict(name='abhishek', city='gwalior', job='coder')
new_person = {f"{k[0].upper()}{k[1:]}":f"{v[0].upper()}{v[1:]}" for k,v in person.items()}
print(new_person)

"""
CONDITIONAL LOGIN WITH DICTIONARIES
"""
x = {num:("even" if num % 2 == 0 else "odd") for num in range(0, 10)}
print(x)

z = {(k.upper() if k is 'name' else k):v for k,v in person.items()}
print(z)