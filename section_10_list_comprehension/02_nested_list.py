# Nested List

"""
NESTED LIST:
    --> List inside a List is called Nested List.
    --> Multidimensional List
    --> Complex Data Structures - Matrices
    --> Game Boards / Mazes
    --> Rows and Columns for visualizations, tabulation and grouping data.
"""
profile = ['Abhishek Baghel', 21, ['Programming', 'Music', 'Maths'], ['Gwalior', 'MP', 'Country']]

print(profile[2])
print(profile[2][1])
print(profile[3][-1])

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)

for x in nested_list:
    for y in x:
        print(y)

for x in nested_list:
    print(f"{x[0]} {x[1]} {x[2]}")

for x in nested_list:
    res = ""
    for y in x:
        res += f"{y} "
    print(res)

"""
Nested List Comprehension
"""
z = [[y*y for y in x] for x in nested_list]
print(z)

a = [[y**2 if y % 2 == 0 else y**3 for y in x] for x in nested_list]
print(a)

b = [["O" if y % 2 == 0 else "X" for y in range(1, 4)] for x in range(1, 4)]
print(b)

"""
Making a Nested List Using range
"""
nested_using_range = [[y for y in range(1, 4)] for x in range(1, 10)]
print(nested_using_range)