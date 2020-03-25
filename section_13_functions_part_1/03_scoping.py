# Scope

"""
SCOPE:
    --> Where Our Variables Can Be Accessed!
    --> Variables Created In Functions are Scoped in that function!
    --> Global Scope is Available For All Scopes But Local Scope is Availabe Only For That Block Only.
    --> global keyword - tells a function to use global variable instead of local variable.
    --> nonlocal keyword - Lets us modify a parent's variables in a child(aka nested) function
"""

def dummy():
    number = 4
    print(f"Lucky Number: {number}")

dummy()
# print(number) - Can't Run Cause It is scoped to function dummy. {Local Scope}

name = 'Abhishek'
def say_hi():
    # name += ' Baghel' - Give Error Because It thinks name is local variable but it a global variable. To Use it use following way.
    global name
    name += ' Baghel'
    print(f"Hello {name}")

say_hi()

def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner()
print(outer())