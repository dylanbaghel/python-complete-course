import json

data = json.dumps({'name': 'Abhishek Baghel', 'email': 'abhi@gmail.com'})

print(data)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"{self.name} is {self.age} Year(s) old."

person1 = Person("Abhishek Baghel", 21)
data1 = json.dumps(person1.__dict__)
print(data1)

"""
Can Use 'jsonpickle' module from pip to 'encode' and 'decode' json files.
"""