"""
Higher Order Function:
    --> We Can Pass function as argument to other functions.
    --> We can return a function from other function.
"""

# Passing function as argument
def user(id, func):
    if id < 10:
        func('Not Found', None)
        return
    func(None, { 'id': id, 'name': 'Abhishek' })

def foundUser(err, user):
    if (err):
        print(err)
    else:
        print(user)

user(23, foundUser)

# Returning a function from a function
def create_user(user_name):
    def creating_user():
        return f"{user_name} Created."
    return creating_user

user = create_user('Abhishek')
print(user())