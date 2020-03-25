# any() & all() Functions

"""
all:
    --> Return True if all elements of the iterable are truthy(or if the iterable is empty)
"""

print(all([0, 1, 2, 3]))

names = ['Abhishek', 'Aakash', 'Abhinav', 'Abhisar', 'Akull', 'Akhil']
is_all_names_start_with_A = all([name[0] == 'A' for name in names])
print(is_all_names_start_with_A)

names.append('Kora')
is_all_names_start_with_A = all([name[0] == 'A' for name in names])
print(is_all_names_start_with_A)


"""
any():
    --> Return True if any element of the iterable is truthy. If the iterable is empty, return False.
"""
print(any([0, 1, 2, 3]))

names = ['Abhishek', 'Baghel', 'Kora', 'Jen', 'Zimi']
is_any_name_start_with_A = any([name[0] == 'A' for name in names])
print(is_any_name_start_with_A)