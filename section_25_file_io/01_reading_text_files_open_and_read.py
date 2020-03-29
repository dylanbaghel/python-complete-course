"""
Reading Files:
    --> We Can Read a File With The 'open' function.
    --> 'open' returns a file object to you.
    --> we can read a file object with the 'read' method.
    --> Python Reads a Files By Using a Cursor.
    --> After a File is read, the cursor is at the end.
    --> To move the cursor, use the 'seek' method.
"""
file = open('file.txt')
print(file.read())

# Move Cursor At The Start
file.seek(0)

print(file.read())

file.seek(0)

# Read Line By Line
print(file.readline())
# Next Line
print(file.readline())

file.seek(0)

# Read All Lines --> Returns a list of all the lines.
print(file.readlines())

file.seek(0)


"""
Closing a File:
    --> We can close a file with the 'close' method.
    --> We can check if a file is closed with the closed attribute.
    --> Once closed, a file can't be read again.
    --> Always close files - it frees up system resources!
"""
print(file.closed)
file.close()
print(file.closed)

print(file.read())


