"""
@property:
    --> This decorator can be used to make properties which behave as getter.
@var_name.setter:
    --> This decorator is used to create setter property.
"""

class Human:
    def __init__(self, first, last, age):
        self._first = first
        self._last = last
        self._age = age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("age cannot be negative")
    
    @property
    def full_name(self):
        return f"{self._first} {self._last}"
    

abhishek = Human('Abhishek', 'Baghel', 21)
print(abhishek.age)
abhishek.age = 22
print(abhishek.age)
print(abhishek.full_name)