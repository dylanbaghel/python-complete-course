# Raising Own Errors

"""
In python we can also throw errors using the raise keyword. This is helpful when creating our own kinds of exception and error messages.
"""

def colorize(text, color):
    colors = ('cyan', 'red', 'blue', 'green', 'coral', 'magents')
    if type(text) is not str:
        raise TypeError('text must be instance of str')
    if type(color) is not str:
        raise TypeError('color must be string')
    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printed {text} in {color}")

colorize('Hello', 'blue')

raise ValueError('Error Message')
raise KeyError('Key Error Message')
raise IndexError()
raise ZeroDivisionError()
raise AttributeError()
raise TypeError()