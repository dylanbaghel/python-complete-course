# Parameter Ordering

"""
Parameters Ordering:
    --> Normal Positional Parameters
    --> *args
    --> Default Parameters
    --> **kwargs
"""

def display_info(a, b, *args, name="Abhishek Baghel", **kwargs):
    return [a, b, args, name, kwargs]

print(display_info(1, 5, 121, job="Programmer", name="Dylan Baghel"))