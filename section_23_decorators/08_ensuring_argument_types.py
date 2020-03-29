# Exercise

"""
Exercise --> Enforcing Types of Argument
"""

def enforce(*types):
    def inner(fn):
        def wrapper(*args, **kwargs):
            # convert args into something mutable
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append(t(a))
            return fn(*newargs, **kwargs)
        return wrapper
    return inner

@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)

repeat_msg('Hi There', '2')