# Dictionary Unpacking

"""
Dictionary Unpacking:
        --> We can use ** as an argument to a function to "unpack" values.
"""

def profile(**kwargs):
    print(kwargs)

details = {
    'name': 'Abhishek',
    'age': 21,
    'hobbies': ['Programming']
}

profile(**details)

def profile2(name, age):
    print(f"{name} is {age} Year(s) Old.")

details2 = {
    'name': 'Abhishek Baghel',
    'age': 21
}

profile2(**details2)

def add_and_multiply_numbers(a, b, c, **kwargs):
    print(a + b * c)
    print("Other Stuff...")
    print(kwargs)

data = dict(a=1, b=2, c=3, d=55, name="Jonas")

add_and_multiply_numbers(**data, color="green")