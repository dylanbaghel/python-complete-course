# Set

"""
SETS:
    --> Set is a collection which is unordered and unindexed. No duplicate members.
    --> Sets are like formal mathematical sets.
    --> Sets do not have duplicate values.
    --> Elements in sets aren't ordered.
    --> You Cannot access items in a set by index, because there is no order.
    --> Sets can be useful if you need to keep track of a collection of elements, but don't care about ordering, keys or values and duplicated.
"""
s = {1, 1, 1, 5, 5, 6, 9, 77, 77, 8, 9} # Duplicates Will Be Eliminated.
print(s)

# s[0] -> Not Possible, indexing can't be used in sets.

print(1 in s)

"""
Iterating Over Sets
"""
for i in s:
    print(i)

"""
Removing Duplicates From List
"""
cities = ["Gwalior", "Morena", "Gwalior", "Jaipur", "Mathura", "Mathura", "Delhi", "Mumbai", "Delhi", "Ahmedabad"]
cities = list(set(cities))
print(cities)

"""
Set Methods:
    --> add(x) - Adds an element to a set. If the element is already in the set, the set doesn't change.
    --> remove(x) - Removes a value from the set - returns a KeyError if the value is not found.
    --> discard(x) - Also Removes a value from the set but doesn't throw error in case of value is not found.
    --> copy() - Creates a copy of the set.
"""

# Copy
cities = {"Gwalior", "Morena", "Gwalior", "Jaipur", "Mathura", "Mathura", "Delhi", "Mumbai", "Delhi", "Ahmedabad"}
cities_not_copy = cities
cities_copy = cities.copy()
print(cities_not_copy is cities)
print(cities_copy is cities)

# Add
cities.add('New City')
print(cities)

# Remove
cities.remove("New City")
print(cities)

# cities.remove("Gurgaon") - Throws Key Error Because It is not found.

# Discard
cities.discard("Gurgaon") # Doesn't Throw Error 

"""
Sets Maths Methods:
    --> Union(|), Intersection(&)
"""
math_students = {"Abhishek", "Dylan", "Bittu", "Kora", "Jen"}
biology_students = {"Mike", "Abhishek", "Scarlett", "David", "Oliver Queen", "Kora"}

union = math_students | biology_students
print(union)

intersection = math_students & biology_students
print(intersection)

"""
Set Comprehension:
    --> We Can Use Comprehension With Sets.
"""
x = {0, 1, 2, 3, 4, 5, 5, 6, 6, 7, 7, 7}
u = {i ** 2 for i in x}
print(u)
