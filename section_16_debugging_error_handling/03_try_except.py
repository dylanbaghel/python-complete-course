# try, except

"""
Handle Errors:
    --> In Python, it is strongly encouraged to use try/except blocks, to catch exceptions where we can do something about them.
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


try:
    colorize('Hello', 'cora')
except TypeError as err:
    print(err)
except ValueError as err:
    print(err)

print('After Try/Except Block')
