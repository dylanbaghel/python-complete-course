# Swapping Values

"""
SWAPPING VALUES
"""

# Python Way
names = ['Abhishek', 'Dylan']
print(names)
names[0], names[1] = names[1], names[0]
print(names)

# Normal Way - Using Temp Variable
names = ['Abhishek', 'Dylan']
x = names[0]
names[0] = names[1]
names[1] = x
print(names)