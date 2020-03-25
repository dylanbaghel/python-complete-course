"""
__repr__():
    --> The __repr__ method is one of several ways to provide a nicer string repesentation.
"""

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"{self.name} is {self.age}"

user = User('Abhishek Baghel', 21)
print(user)