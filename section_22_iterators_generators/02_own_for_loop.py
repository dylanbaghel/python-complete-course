"""
Own Version of For Loop:
    --> To Demonstrate The Use of Iterators.
"""

def my_for(iterable, fn):
    iterator = iter(iterable)
    while True:
        try:
            fn(next(iterator))
        except StopIteration:
            break


my_for(['Abhishek', 'Dylan', 'Bittu'], lambda name: print(f"Hello, {name}"))