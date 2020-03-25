# Slices

"""
SLICE:
    --> Slice is a way to grab the subset of any string or list.
    --> list[start:end:step]
    --> Slicing Always Returns The New List It Never Modifies The Original List. It is also a way to make copy of list along with copy() method.
    --> End Index is Exclusive
"""

message = 'Abhishek Baghel Loves Programming'
print(message[4:])  # Start From Index 4 and End At The Last Index.
# Start From Index 3 and End At Index 16 and take jumps of 1.
print(message[3:16])
# Start From Index 0 and End At Index 16 and take jumps of 2.
print(message[:16:2])
# Start From Index 0 and End At The Last Index and take jumps of 1 but in reverse order.
print(message[::-1])

names = ['Abhishek', 'Dylan', 'Jonas', 'Bittu', 'Jen', 'Brad', 'Max',
         'Andrew', 'Hem', 'Heam', 'Kr$na', 'Void', 'Bella', 'Talha']
print(names[4:])
print(names[3:7])
print(names[:11:2])
print(names[::-1])
print(names[2][::-1]) # Select Index 2 Item Which is String 'Jonas', then reverse it using slice.

"""
TRICKS WITH SLICES:
    --> Reversing List/String:
        --> string/list[::-1]
    --> Modifying Portion of List:
        --> numbers = [1, 2, 3, 4, 5]
            numbers[1:3] = ['a', 'b', 'c']
            print(numbers)
"""
numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers[1:3] = ['a', 'b', 'c']
print(numbers)
