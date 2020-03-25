# Lists 

"""
LISTS:
    --> List is a reference data type.
    --> List is a collection which is ordered and changeable. Allows duplicate members
"""

"""
Creating List
"""
shopping_cart = ['Bananas', 'Apple', 'Oranges', 'Spinach']
print(shopping_cart)

"""
Accessing Items in Lists:
    --> We Can Access data in list using indexing. indexing is zero based
"""
print(shopping_cart[0])
print(shopping_cart[1])

"""
Length of The List:
    --> len() method returns the length of list.
"""
print(len(shopping_cart))

"""
Creating List of Numbers Using range()
"""
numbers = list(range(1, 10))
print(numbers)

"""
Check if item in list
"""
if 'Bananas' in shopping_cart:
    print('Good Choice')


"""
Iterating List
"""
for item in shopping_cart:
    print(item)

i = 0
while i < len(shopping_cart):
    print(shopping_cart[i])
    i += 1

"""
List Methods:
    --> append() - Add Single Item To The End of List
    --> insert() - Add Single Item At the given indexed position
    --> extend() - Takes List as input, iterate over it to add each item of the argument list to the targeted list.
"""
names = ['Abhishek', 'Dylan', 'Bittu']
print(names)

# Append
names.append('Jonas')
print(names)

# Insert
names.insert(2, 'Brad')
print(names)

# Extend
names.extend(['Kora', 'Jen'])
print(names)

"""
LIST METHODS:
    --> clear() - Remove all items from the list
    --> pop() - if no argument passed then REMOVE LAST ITEM but if index is passed as argument then REMOVE THE GIVEN INDEX POSITIONED ITEM. It returns deleted item.
    --> remove() - Takes Actual Value as an argument and delete the first occurrence of that argument in the list.
"""

# clear
names.clear()
print(names)

names = ['Abhishek', 'Dylan', 'Bittu', 'Jonas', 'Kora', 'Jen', 'Brad', 'Max']
print(names)

# pop
names.pop()
print(names)

names.pop(1)
print(names)

deleted_item = names.pop()
print(deleted_item)
print(names)

# Remove
names.remove('Bittu')
print(names)

"""
LIST METHODS:
    --> index() - returns the index of the specified item in the list. In index() method we can specify start and end arguments -> which start the iteration from the start index and end at the end index.
    --> count(x) - Returns The Number of Occurrences of x in the list.
    --> reverse() -> Reverse The Items of List in-place.
    --> sort() -> Sort The Items of The List in-place.
    --> join() --> It is a string method which joins the items of a list with a separator.
"""
names = ['Abhishek', 'Dylan', 'Bittu', 'Jonas', 'Kora', 'Jen', 'Brad', 'Max']
print(names)
numbers = [5,5,5,6,8,9,8,7,6,5,9,1]
print(numbers)

# Index
found_index = names.index('Jen')
print(found_index)
print(numbers.index(5)) # Returns Index of First Occurrence of 5.
print(numbers.index(9, 6)) # Returns Index of First Occurence of 9, but start the iteration from index 6.
print(numbers.index(6, 4, 10)) # Returns Index of First Occurence of 6, but start from index 4 and end at 10 index.

# Count
print(numbers.count(5)) # Returns The Number of Occurrences of 5 in the list.

# Reverse
names.reverse() # Reverse The Items in-place
print(names)

# Sort
names.sort() # Sort The Items In Ascending Order in-place
print(names)

# Join
print("-".join(names)) # Join Items of The List With a Separator