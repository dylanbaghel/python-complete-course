"""
Iterators V/S Iterables:
    --> Iterator is an object that can be iterated upon. An object which which returns data, one element at a time when next() is called on it.
    --> Iterable is an object which will return an iterator when iter() is called on it.
    --> When next() is called on an iterator, the iterator returns the next item. It keeps doing so until it raises a StopIteration Error.
    --> For loop pass the iterable to iter() function implicitly.
"""

# Iterable
name = 'Abhishek'
names = ['Abhishek', 'Dylan', 'Jonas']
# Iterator
it = iter(name)
it2 = iter(names)
print(it)

print(next(it))
print(next(it))
print(next(it2))
print(next(it2))