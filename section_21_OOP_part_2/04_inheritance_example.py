class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users."

    def __init__(self, first, last, age):
        self._first = first
        self._last = last
        self._age = age
        User.active_users += 1

    @property
    def full_name(self):
        return f"{self._first} {self._last}"
    
    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"


class Moderator(User):
    total_mods = 0
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self._community = community
        Moderator.total_mods += 1
    
    @classmethod
    def display_active_mods(cls):
        return f"There are currently {cls.total_mods} active mods."

    @property
    def community(self):
        return self._community
    
    def remove_post(self):
        return f"{self.full_name} removed a post from {self.community}"


print(User.display_active_users())
abhishek = Moderator('Abhishek', 'Baghel', 21, 'Technology')
user1 = User("Dylan", "Paul", 18)
print(User.display_active_users())
print(abhishek.display_active_mods())
print(abhishek.full_name)

print(abhishek.community)