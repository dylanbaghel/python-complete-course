"""
Multiple Inheritance:
    --> Python Supported Multiple Inheritance means one child class can have multiple parent class.
    --> class ChildClass(ParentClass1, ParentClass2) --> Here Order is important, first passed class runs first {if super() is used}.
    --> Multiple Inheritance is not used anymore because of diamond problem. Most of the core OOP language don't support it now.

MRO:
    --> Method Resolution Order
    --> Whenever we create a class, Python sets a MRO for that class, which is the order in which Python will look for methods on instances of that class.
    --> We can programmatically reference the MRO three ways:
        --> '__mro__' attribute of the class.
        --> use the 'mro()' method on the class.
        --> use the builtin help(cls) method.
"""

class Aquatic:
    def __init__(self, name):
        print("Aquatic INIT")
        self.name = name
    
    def swim(self):
        return f"{self.name} is swimming"
    def greet(self):
        return f"I am {self.name} of the sea!"

class Ambulatory:
    def __init__(self, name):
        print("AMBULATORY INIT")
        self.name = name
    
    def walk(self):
        return f"{self.name} is walking"
    def greet(self):
        return f"I am {self.name} of the land"
    
class Penguin(Aquatic, Ambulatory):
    def __init__(self, name):
        print("PENGUIN INIT")
        super().__init__(name=name)


captain = Penguin('Captain')
print(Penguin.__mro__)
print(Penguin.mro())
print(help(Penguin))