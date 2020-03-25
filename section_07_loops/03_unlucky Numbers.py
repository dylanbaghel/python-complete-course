# Unlucky Numbers

"""
EXERCISE --> UNLUCKY NUMBERS
"""
for num in range(1, 21):
    if num == 3 or num == 13:
        nature_of_number = 'Unlucky'
    elif num % 2 == 0:
        nature_of_number = 'Even'
    else:
        nature_of_number = 'Odd'
    
    print(f"{num} is {nature_of_number}")