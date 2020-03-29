"""
Why Test:
    --> Reduce bugs in existing code.
    --> Ensure bugs that are fixed stay fixed.
    --> Ensure that new features don't break old ones.
    --> Ensure that cleaning up code doesn't introduce new bugs.

TDD:
    --> Test Driven Development.
    --> Development begins by writing tests.
    --> Once tests are written, write code to make tests pass.
    --> Once tests pass, a feature is considered complete.
    --> RED - Write a test that fails.
    --> GREEN - Write the minimal amount of code necessary to make the test pass.
    --> REFACTOR - Clean up the code, while ensuring that tests still pass.
"""

"""
Assertions:
    --> We can make simple assertions with the `assert` keyword.
    --> 'assert' accepts an expression.
    --> Returns None if the expression is truthy.
    --> Raises an AssertionError if the expression is falsy.
    --> Accepts an optional error message as a second argument.
    --> If a python file is run with the -O flag, assertions will not be evaluated.
    --> Not The Good Way For Testing
"""

def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both Numbers must be positive!"
    return x + y

print(add_positive_numbers(1, 1))
# print(add_positive_numbers(5, -6))


"""
doctests:
    --> We can write tests for functions inside of the docstring.
    --> Write code that looks like it's inside of a REPL.
    --> Command To Run doctests:
            --> python -m doctest -v file_name.py
    --> Extreme Fixed Syntax.
    --> whitespace, no space and extra space after comma in the list, double quoted string, order of the unordered collections, etc. cause problems and evaluate as failure.
"""

def add(a, b):
    """
    >>> add(2, 3)
    5
    >>> add(100, 200)
    300
    """
    return a + b

def double(values):
    """ 
    double the values in a list
    >>> double([1,2,3,4])
    [2, 4, 6, 8]

    >>> double([])
    []

    >>> double(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> double([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * val for val in values]