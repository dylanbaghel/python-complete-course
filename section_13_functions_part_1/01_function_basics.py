# Function

"""
FUNCTION:
    --> A process for executing a task.
    --> It can accept input and return an output.
    --> Useful for executing similar procedures over and over.
    --> Reusable Code.
    --> Stay DRY - Don't Repeat Yourself!
    --> Clean Up and Prevent Code Duplication.
    --> "Abstract Away" code for other users:
            --> Imagine if you had to rewrite the "print()" function for every program you wrote.            
"""

"""
Defining Functions
"""

def greet():
    print("Hi")

"""
Executing Function
"""
greet()
greet() 

"""
Returning a Values From Function
    --> return keyword:
            --> Exits The Function.
            --> Outputs Whatever Value is Placed After The return Keyword.
"""
def print_square_of_7():
    return 7 ** 2

square_of_7 = print_square_of_7()
print(square_of_7)

"""
Parameters
    --> Supports Default Parameters Also.
"""
def add(x, y):
    return x + y

def square(x):
    return x * x

print(add(22, 11))
print(square(64))

# Default Parameters
def cube(x = 2):
    return x ** 3

print(cube(5))
print(cube())

"""
Parameters v/s Arguments:
    --> A parameter is a variable in a method definition.
    --> When a method is called, the arguments are the data you pass into the method's parameters.
    --> Parameter is a variable in the declaration of function.
    --> In Above Example: 'x' is a parameter and data for x is argument.
"""

"""
Keyword Arguments
"""
def full_name(first, last):
    return f"Your Name is {first} {last}"

print(full_name(first="Abhishek", last="Baghel"))
print(full_name(last="Baghel", first="Dylan"))