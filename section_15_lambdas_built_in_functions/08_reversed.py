# reversed() Function

"""
reversed():
    --> Returns a reverse iterator
"""
names = ['Kora', 'Donut', 'Power']
reverse_names_iterator = reversed(names)
print(reverse_names_iterator)

for name in reverse_names_iterator:
    print(name)

print("".join(list(reversed("Abhishek"))))
