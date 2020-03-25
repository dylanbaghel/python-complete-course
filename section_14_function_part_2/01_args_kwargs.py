# args and kwargs

"""
*args:
    --> A special operator we can pass to functions.
    --> Gathers remaining arguments as a tuple.
    --> This is just a parameter - you can call it whatever you want.
    --> args is just a name - we can use any name.
"""

def sum_all_num(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all_num(1, 2, 3, 4, 5))
print(sum_all_num(1, 2, 3, 4, 5, 6, 7, 8, 9))

"""
**kwargs:
    --> A special operator we can pass to functions.
    --> Gathers remaining keyword arguments as a dictionary.
    --> This is jus a parameter - You can call it Whatever you want
    --> kwargs is just a name - we can use any name.
"""
def profile(**kwargs):
    hobbies_text = ""
    if "hobbies" in kwargs.keys():
        for h in kwargs['hobbies']:
            if kwargs['hobbies'].index(h) == len(kwargs['hobbies']) - 1:
                hobbies_text += h
            else:
                hobbies_text += f"{h}, "
    return f"{kwargs['name']} is {kwargs['age']} year(s) old. He Loves {hobbies_text}. He Lives in {kwargs['address']['city']}, {kwargs['address']['state']} {kwargs['address']['country']}"

print(profile(name="Abhishek Baghel", age=21, hobbies=['Programming', 'Music', 'Rap Music'], address={'state': 'MP', 'city': 'Gwalior', 'country': 'India'}))

def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s Favourite Color is {color}")

fav_colors(abhishek="Red", jonas="green", nalini="coral", ken="forestgreen")