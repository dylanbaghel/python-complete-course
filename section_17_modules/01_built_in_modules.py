"""
MODULE:
    --> Keep Python Files Small.
    --> Reuse Code Across Multiple Files By Importing.
    --> A Module Is Just A Python File.
Ways To Import:
    --> import module_name
    --> import module_name as alias
    --> from module_name import specfic_function
    --> from module_name import *
    --> from module_name import specific_function as alias
"""

"""
BUILT-IN MODULES
"""
import random

# import random as rd

from random import randint

print(random.choice(['apple', 'banana', 'grapes', 'guvava', 'papaya']))

print(randint(0, 9))