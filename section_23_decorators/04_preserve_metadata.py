"""
When We Make High Order Functions (Decorators) then the lower function metadata {such as docstring, __name__ etc.} is lost. To preserve this metadata use `wraps decorator` from the functools
"""

from functools import wraps

def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I AM WRAPPER FUNCTION"""
        print(f"You are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper

@log_function_data
def add(x,y):
    """Add Two Numbers Together"""
    return x + y

print(add(5, 6))

# Without Using `wraps decorator` add function lost its metadata instead its showing the metadata of wrapper function.
# Using `wraps decorator` add function preserves its metadata.
print(add.__name__)
print(add.__doc__)