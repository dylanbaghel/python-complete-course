# Tuple

"""
TUPLE:  
    --> An ordered collection or grouping of items!.
    --> var_name = (a, b, c, d).
    --> Tuple is Immutable - can NEVER be changed!.
    --> Tuples are faster than lists.
    --> It makes your code safer.
    --> Valid Keys in a dictionary.
    --> Some methods return them to you - like .items() method when working with dictionaries.
    --> It's Best When Using as Enumeration.
    --> Can Use Slices Like Lists.
"""

"""
Creating Tuple:
    --> Two Ways:
        --> () sytnax.
        --> tuple() function
"""
x = (1, 2, 3)
print(x)

y = tuple(['Abhishek', 'Dylan'])
print(y)

# Access Data
print(x[0])

# x[1] = 6 - It Fails Because tuple does not support item assignment (Immutable in a nutshell)

months = ('January', 'February', 'March', 'April', 'May')
print(months)

# Tuples can be used as keys in dictionaries
locations = {
    (35.6895, 39.6917): "Tokyo Office",
    (40.7128, 74.0060): "New York Office",
    (37.7749, 122.4194): "San Francisco Office"
}

print(locations[35.6895, 39.6917])

"""
Iterating Over Tuples:
    --> can use for loop to iterate over tuples.
"""
for month in months:
    print(month)

"""
Tuples Built-In Methods:
    --> 1. count(x) -> Returns Number of occurrences of x in the targeted tuple.
    --> 2. index(x) -> Return Index First Occurrence of given value(x).
"""
z = (1, 2, 3, 3, 3, 5, 5, 6, 6, 6, 6)
print(z.count(1))
print(z.count(3))
print(z.count(6))

print(z.index(6))

"""
Nested Tuples
"""
nested_tuple = (1, 2, 3, ('Programming', 'Music'))
print(nested_tuple)
