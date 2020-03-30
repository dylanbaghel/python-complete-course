"""
Pickling:
    --> It's a way to store python objects in a file. It serializes the data in bytestream and we can desearialize it when we need it.
    --> 'wb' - flag is used to write file because b stands for binary to searialize the data in bytestream.
"""

import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"{self.name} is {self.age} Year(s) old."

person1 = Person("Abhishek Baghel", 21)
print(person1)

# Serialize
with open('persons.pickle', 'wb') as file:
    pickle.dump(person1, file)

# Deserialize
with open('persons.pickle', 'rb') as file:
    read_person = pickle.load(file)
    print(read_person)