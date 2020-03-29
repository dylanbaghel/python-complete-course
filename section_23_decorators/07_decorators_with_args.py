"""
We Can Pass Arguments To The Decorator, To Do So We Need An Extra Layer of innder function that accepts the arguments.
"""
from functools import wraps

def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                return f"First arg needs to be {val}"
            return fn(*args, **kwargs)
        return wrapper
    return inner

@ensure_first_arg_is('banana')
def fav_foods(*foods):
    return foods

print(fav_foods('banana', 'rajma'))
print(fav_foods('rice', 'pav bhaji'))

