# Tuple Unpacking

"""
Tuple Unpacking:
    --> We can use * as an argument to a function to "unpack" values.
"""

def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    return total

nums = [1, 2, 3, 4, 5, 6]
numbers = (7, 8, 9, 10)
print(sum_all_values(*nums))
print(sum_all_values(*numbers))