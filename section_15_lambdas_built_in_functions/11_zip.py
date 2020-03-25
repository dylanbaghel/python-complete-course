# zip() Function

"""
zip():
    --> The purpose of zip() is to map the similar index of multiple containers so that they can be used just using as single entity.
"""

"""
zipping
"""
names = ['Abhishek', 'Jonas', 'Kora']
marks = [90, 55, 78]
first_zip = zip(names, marks)
print(list(first_zip))

# initializing lists 
name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ] 
roll_no = [ 4, 1, 3, 2 ] 
marks = [ 40, 50, 60, 70 ] 

# using zip() to map values 
mapped = zip(name, roll_no, marks) 

# converting values to print as set 
mapped = set(mapped) 

# printing resultant values 
print (f"The zipped result is : {mapped}")

"""
Unzipping
"""
name, roll_no, marks = zip(*mapped)
print(name)
print(roll_no)
print(marks)
