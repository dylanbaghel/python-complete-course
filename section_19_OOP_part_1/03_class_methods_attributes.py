"""
Class Attributes:
    --> This attribute belongs to whole class not to the instance and this attribute is shared by all instances of a class and the class itself.

Class Methods:
    --> Class methods are methods (with the @classmethod decorator) that are not concerned with instances, but the class itself.
"""


class User:

    active_users = 0
    db_users = []

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
        User.db_users.append(first.lower())

    @classmethod
    def display_active_users(cls):
        return f"Users Online: {cls.active_users}"
    
    @classmethod
    def find_by_first_name(cls, first):
        if first.lower() not in cls.db_users:
            raise ValueError(f"{first} Not found in our database.")
        return "Found"
    
    @classmethod
    def from_string(cls, csv_str):
        first, last, age = csv_str.split(',')
        return cls(first, last, int(age))



    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}"

    def likes(self, thing):
        return f"{self.first} likes {thing}."

    def is_senior(self):
        return self.age >= 60
    def logout(self):
        User.active_users -= 1
        User.db_users.remove(self.first.lower())
        return f"{self.first} is logged out."

print(User.active_users)
user1 = User('Abhishek', 'Baghel', 22)
print(User.active_users)
user2 = User('Dylan', 'Baghel', 18)
print(User.active_users)
print(user2.logout())
print(User.active_users)
print(User.display_active_users())

user3 = User('Jonas', 'Will', 29)
user4 = User('Kora', 'Per', 36)
user5 = User('Joe', 'Allen', 44)
print(User.display_active_users())
print(User.db_users)

user6 = User.from_string("Victor,Doom,66")
print(user6.full_name())

print(User.find_by_first_name('jonas'))
print(User.find_by_first_name('glock'))

class Pet:
    allowed = ('cat', 'dog', 'fish', 'rat')
    def __init__(self, name, species):
        if species.lower() not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species
    def set_species(self, species):
        if species.lower() not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.species = species

cat = Pet('Blue', 'Cat')
dog = Pet('Johny', 'dog')
print(dog.species)
dog.set_species('rat')
print(dog.species)
