# Dictionaries

"""
DICTIONARY:
    --> Dictionary is a reference data type.
    --> A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
    --> We can access the items of a dictionary by referring to its key name, inside square brackets.
    --> We can change the value of a specific item by referring to its key name
"""
person = {
    'first_name': 'Abhishek',
    'last_name': 'Baghel',
    'age': 21,
    'address': {
        'city': 'Gwalior',
        'state': 'MP',
        'country': 'India'
    }
}
print(person)

person2 = dict(first_name='Abhishek', last_name='Baghel', age=21,
               address=dict(city='Gwalior', state='MP', country='India'))
print(person2)

"""
ACCESSING DATA IN DICTIONARIES
"""
print(person['first_name'])
print(person['address']['state'])


"""
ITERATING DICTIONARIES
    .values() -> Returns values list.
    .keys() -> Returns keys list.
    .items() -> Returns list of tuples containing key and value both.
"""

# Accessing Values
for value in person.values():
    print(value)

# Accessing Keys
for key in person.keys():
    print(key)

# Accessing Values and Keys Both
for key, value in person.items():
    print(f"{key}: {value}")

print(person.items())

"""
TESTING THE EXISTENCE OF ANY KEY OR VALUE IN DICTIONARY
"""
# Checking Keys
print("first_name" in person)
print("phone" in person)

# Checking in values
print("Abhishek" in person.values())

"""
DICTIONARY METHODS:
    --> clear() -> Clear The Whole Dictionary and make it empty.
    --> copy() -> Make a copy of the dictionary.
    --> fromkeys() -> Creates key-values pairs from comma separated values. Any Iterable will work here, lists, strings, range, tuples etc.
    --> get() -> Retrieves a key in an object and return None instead of KeyError if the key does not exist.
    --> pop() -> Takes a single argument corresponding to a key and removes that key-value pair from the dictionary. Returns the value corresponding to the key that was removed.
    --> popitem() -> Removes Random key in a dictionary.
    --> update() -> Update keys and values in a dictionary with another set of key value pairs.
"""
# Clear
person.clear()
print(person)

# Copy
clone = person2.copy()

print(person2 == clone)
print(person2 is clone)

# fromkeys
person4 = {}.fromkeys(['first_name', 'last_name', 'age'], 'unknown')
print(person4)

# get
print(person2.get('first_name'))
print(person2.get('phone'))

# pop
d = person2.pop('age')
print(person2)
print(d)

# popitem
e = person2.popitem()
print(e)
print(person2)

# update
person = {
    'first_name': 'Abhishek',
    'last_name': 'Baghel',
    'age': 21,
    'address': {
        'city': 'Gwalior',
        'state': 'MP',
        'country': 'India'
    }
}
print(person)

updated_data = {
    'first_name': 'Dylan',
    'hobbies': ['Programming', 'Music']
}
person.update(updated_data)
print(person)