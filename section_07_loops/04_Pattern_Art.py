# Exercise

"""
EXERCISE - Pattern ART
"""

rows = int(input('How Many Rows Do You Want: '))

print("\n***** For Loop *****")
for n in range(1, rows + 1):
    print("*" * n)

print("\n***** While Loop *****")
counter = 1

while counter <= rows:
    print("*" * counter)
    counter += 1

print("\n***** Reverse *****")
for n in range(rows, 0, -1):
    print("*" * n)

print("\nMIRROR")
x = 1
spaces = rows - 1
result = ""

while spaces >= 0:
    result += " " * spaces
    result += "*" * x
    x += 1
    spaces -= 1
    print(result)
    result = ""

print("\n Mirror Using Inner Loops")
res = ""

for i in range(0, rows + 1):
    for j in range(0, rows - i):
        res += " "
    for k in range(i):
        res += "*"
    print(res)
    res = ""


