from functools import wraps

def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError('No kwargs allowed')
        return fn(*args, **kwargs)
    return wrapper

@ensure_no_kwargs
def greet(name):
    print(f"Hi There, {name}")

def message(msg):
    print(msg)

message = ensure_no_kwargs(message)
message('This is my message')

greet("Abhishek")
greet(name="Abhishek")