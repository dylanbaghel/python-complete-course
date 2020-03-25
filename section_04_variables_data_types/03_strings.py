# Strings

"""
Strings Can Be Declared Using 'Single quotes' or "Double quotes"
"""

"""
Escaping Character - "'\'"
 --> It means escape the special nature of that character.
"""

msg = 'Hello You\'re going to this challenge.'
print(msg)

"""
String Concatenation
    --> Three Ways
    --> 1. Using '+' Operator
    --> 2. Using 'f String'
    --> 3. Using 'format() method' {Python 2 --> 3.5}
"""
first_name = 'Abhishek'
last_name = 'Baghel'
full_name = first_name + ' ' + last_name
print(full_name)
full_name = f"{first_name} {last_name}"
print(full_name)
print("Hello, {}".format(full_name))

"""
String Appending:
    --> Using '+=" Operators
"""
msg = "hello"
msg += f" {full_name}"
print(msg)


"""
String Index
    --> Similar To Array We Can Use Index Features With Strings
    --> Indexing is 'ZERO' Based
    --> Negative Indexing Perform In The Reverse Order
"""
full_name = 'Joker Jen'
print(full_name[2])
print(full_name[-1])
