"""
Class:
    --> __init__() -> Classes in python have a special __init__ method, which gets called every time we create an instance of the class (instantiate). {constructor}

    --> _variable_name -> convention to make private member variables.
    --> __variable_name -> To avoid name conflict in inheritance. Name Mangling done by python.
    --> Dunder Methods
"""
class User:
    pass

user = User()
print(user)
print(type(user))

class Person:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.__msg = 'This is message!'
    
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}"
    def likes(self, thing):
        return f"{self.first} likes {thing}."
    def is_senior(self):
        return self.age >= 60

person1 = Person('Abhishek', 'Baghel', 22)
person2 = Person('Dylan', 'Baghel', 18)
person3 = Person('Jen', 'Williams', 69)
print(person1.first, person1.age)
print(person2.first, person2.age)
# Name Mangling
print(person1._Person__msg)

# Instance Methods
print(person2.full_name())
print(person1.initials())
print(person2.likes('Programming'))
print(person1.is_senior())
print(person3.is_senior())