# Rock Paper Scissor - Computer Version

import random

print(".....rock.....")
print(".....paper....")
print(".....scissor......")

choices = ['rock', 'scissor', 'paper']
computer_choice = choices[random.randint(0, 2)].lower()
player_choice = input("Enter Player's choice: ").lower()

result = None

if computer_choice not in choices or player_choice not in choices:
    print('Invalid Option')
elif computer_choice == player_choice:
    print(f"Computer's Move: {computer_choice}")
    print('TIE')
else:
    if computer_choice == 'rock':
        if player_choice == 'paper':
            result = 'Player Wins'
        elif player_choice == 'scissor':
            result = 'Computer Wins'
    elif computer_choice == 'paper':
        if player_choice == 'rock':
            result = 'Computer Wins'
        elif player_choice == 'scissor':
            result = 'Player Wins'
    elif computer_choice == 'scissor':
        if player_choice == 'rock':
            result = 'Player Wins'
        elif player_choice == 'paper':
            result = 'Computer Wins'
    else:
        print('Invalid Option')

if (result):
    print(f"Computer's Move: {computer_choice}")
    print('SHOOT!')
    print(result)