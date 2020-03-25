# CONDITIONALS 

"""
    CONDITIONALS:
        --> IF
        --> IF - ELSE
        --> IF - ELSE IF - ELSE IF... ELSE
        --> TERNARY
    Empty Objects, Empty String, None and Zero evaluated as False by defaul
"""

"""
    COMPARISON OPERATORS:
        --> '== OR is' --> Equal To
        --> '>' --> Greater Than
        --> '>=' --> Greater Than and Equal To
        --> '<' --> Less Than
        --> '<=' --> Less Than and Equal To
        --> '!=' --> Not Equal To   
"""

"""
IF STATEMENTS:
    if condition:
        do something
"""
name = 'Abhishek'
if name.lower() == 'abhishek':
    print('Hey Correct Name: ' + name);

"""
IF-ELSE STATEMENTS:
    if condition:
        do something
    else:
        do something else
"""
if name.lower() == 'dylan':
    print('Correct Name')
else:
    print('Incorrect Name')

"""
IF-ELIF STATEMENTS
    if condition:
        do something
    elif another condition:
        do something
    elif some other condition:
        do something
    else:
        default something    
"""
day = 'SUn'
message = "It's "
if day.lower() == 'mon':
    message += 'Monday'
elif day.lower() == 'tue':
    message += 'Tuesday'
elif day.lower() == 'wed':
    message += 'Wednesday'
elif day.lower() == 'thu':
    message += 'Thursday'
elif day.lower() == 'fri':
    message += 'Friday'
elif day.lower() == 'sat':
    message += 'Saturday'
elif day.lower() == 'sun':
    message += 'Sunday'
else:
    message = 'Invalid Option'

print(message)

"""
is V/S ==
    --> The == operator compares the values of both the operands and checks for value equality. Whereas is operator checks whether both the operands refer to the same object or not.
"""

list1 = [] 
list2 = [] 
list3=list1 
  
if (list1 == list2): 
    print("True") 
else: 
    print("False") 
  
if (list1 is list2): 
    print("True") 
else: 
    print("False") 
  
if (list1 is list3): 
    print("True") 
else:     
    print("False") 


"""
LOGICAL OPERATORS:
    --> 'and' --> {True, True}
    --> 'or' --> {True, False} - {False, True}
    --> 'not' --> Logical Negation 
"""
age = 12
name = 'abhishek'

if (name == 'abhishek') or (age > 16 and age < 60):
    print("Can Participate In Race")
else:
    print("Cannot Participate In Race")

if not (name == 'abhishek'):
    print('Allowed')
else:
    print(f"{name} is Blocked")


"""
TERNARY
    --> [on_true] if [Expression] else [on_false]
"""
name = 'jenn'
message = "You're Allowed" if name == 'joker' else "Not Allowed"
print(message)