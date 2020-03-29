# Exercise

"""
Exercise --> Building Speed Test Decorator
"""
from functools import wraps
from time import time

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Executing: {fn.__name__}")
        print(f"Time Elapsed: {end_time - start_time}")
        return result
    return wrapper

@speed_test
def sum_nums_using_generator():
    return sum(x for x in range(100000000))

print(sum_nums_using_generator())

@speed_test
def sum_nums_using_list():
    return sum([x for x in range(100000000)])

print(sum_nums_using_list())