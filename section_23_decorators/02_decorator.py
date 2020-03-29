"""
Decorator:
    --> Decorators are functions.
    --> Decorators wrap other function and enhace their behaviour.
    --> Decorators are examples of higher order functions.
    --> Decorators have their own syntax, using '@' (syntactic sugar)
"""

def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day")
    return wrapper

def greet():
    print('My Name is Abhishek')

def rage():
    print('I Hate You')

# Without Decorators
greet = be_polite(greet)
rage = be_polite(rage)
greet()
rage()

# With Decorators
@be_polite
def power():
    print('Power Full Person')

power()