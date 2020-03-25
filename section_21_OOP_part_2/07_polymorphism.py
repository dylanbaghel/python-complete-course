"""
Polymorphism:
    --> A key principle in OOP is the idea of polymorphism - an object can take on many(poly) forms(morph).
    --> Here are two important practical applications:
        --> 1. The same class method works in a similar way for different classes.
        --> 2. The same operation works for different kinds of objects.
"""

"""
1. The same class method works in a similar way for different classes:
    Polymorphism & Inheritance:
        --> A common implementation of this is to have a method in a base(or parent) class that is overridden by a subclass. This is called method overriding.
        --> Each subclass will have a different implementation of the method.
"""

class Animal():
    def speak(self):
        raise NotImplementedError("Subclass needs to implemnt this method")

class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "MEOW"

class Duck(Animal):
    def speak(self):
        return "Quack"

d = Dog()
print(d.speak())
c = Cat()
print(c.speak())

"""
2. The same operation works for different kinds of objects {Special Methods}:
    --> e.g. The + operator is shorthand for a special method called __add__() that gets called on the first operand. If the first(left) operand is an instance of int, __add__() does mathematical addition. If it's a string, it does string concatenation.
    --> Therefore, we can declare special methods on our own classes to mimic the behavious of builtin objects, like so using __len__.
"""

class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    
    def __repr__(self):
        return f"Human Named {self.first} {self.last} aged: {self.age}"
    def __len__(self):
        return self.age
    
    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first='Newborn', last=self.last, age=0)
        raise TypeError('Please Add Human To Human')
    
    def __mul__(self, num):
        if isinstance(num, int):
            return [self for i in range(num)]
        raise TypeError('Please Multiply a integer')


abhi = Human('Abhishek', 'Baghel', 21)
nalini = Human('Nalini', 'W', 20)
print(abhi)

print(abhi + nalini)
print(abhi * 3)
print((abhi + nalini) * 2)