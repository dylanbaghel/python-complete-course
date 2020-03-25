# lambda

"""
LAMBDAS:
    --> n Python, lambda expressions (or lambda forms) are utilized to construct anonymous functions. To do so, you will use the lambda keyword (just as you use def to define normal functions).
"""

square = lambda num: num * num
print(square(5))

def higher(func, name):
    func(name)

# Without lambda
def greeting(name):
    print(f"Hello, {name}")

higher(greeting, name='Dylan')

# With lambda
higher(lambda name: print("hello " + name), name="Abhishek")

