"""
with Blocks:
    --> Another Way Of Dealing With Files.
    --> Don't Need To Manually Close The File When Using 'with' blocks.
    --> 'with' blocks calls '__exit__' methods after dealing with files, whether it is successfull or failed attempt.
"""

with open('file.txt') as file:
    data = file.read()
    print(data)

print(file.closed)