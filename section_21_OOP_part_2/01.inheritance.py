"""
Inheritance:
    --> A key feature of OOP is the ability to define a class which inherits from another class (a "base" or "parent" class).
"""
class Animal:
    def make_sound(self, sound):
        print(f"this animal says {sound}")

class Cat(Animal):
    pass

cat = Cat()
cat.make_sound('MEOW')

print(isinstance(cat, Cat))
print(isinstance(cat, Animal))