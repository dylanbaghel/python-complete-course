"""
Writing Files:
    --> We can also use 'open' to write a file.
    --> Need to specify the 'w' flag as the second argument.
    --> Writes With Files Using 'w' overrides the content of the files.
"""

with open('story.txt', 'w') as file:
    file.write('Abhishek Baghel is The Amazing Person\n' * 10)

"""
Modes For Opening Files:
    --> 'r' - default, to read files.
    --> 'w'- to write files, but override content.
    --> 'a' - append, append content at the end of the files (No Control Over Cursor)
    ---> 'r+' - Read and wirte to a file (writing based on cursor), It does not create a new file if not existed.
"""
with open('hell.txt', 'a') as file:
    file.write('Abhishek Baghel is The Amazing Person\n' * 10)

with open('new.txt', 'r+') as file:
    file.write(':)')
    file.seek(10)
    file.write('(:')