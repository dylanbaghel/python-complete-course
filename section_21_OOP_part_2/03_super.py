"""
super():
    --> method is used to invoke the parent class constructor.
"""

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy
    
    def play(self):
        print(f"{self.name} plays with {self.toy}")

jen = Cat('Jen', 'Scottish Fold', 'Strings')
jen.play()