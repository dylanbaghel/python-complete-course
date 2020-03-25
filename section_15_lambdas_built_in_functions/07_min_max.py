# min() & max() Functions

"""
min(*args):
    --> returns the least number or least word alphabetically.

max(*args):
    --> returns the max number or least word alphabetically.
"""
nums = [1, 55, 545, 54, 55, -9, -12]
print(min(nums))
print(max(nums))

names = ['Arya', 'Jonas', 'Samson', 'Kora', 'Tim']
max_based_on_length = max(names, key=lambda n: len(n))
print(max_based_on_length)