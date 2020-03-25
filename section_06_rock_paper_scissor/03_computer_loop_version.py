# Rock Paper Scissor - Computer Loop Version

import random

choices = ['rock', 'scissor', 'paper']
is_play = True
player_score = 0
computer_score = 0


while is_play:
    print(".....rock.....")
    print(".....paper....")
    print(".....scissor......")
    result = None
    computer_choice = choices[random.randint(0, 2)].lower()
    print(computer_choice)
    player_choice = input("Enter Player's choice ('q' or 'quit' to Exit): ").lower()

    if player_choice == 'quit' or player_choice == 'q':
        is_play = False
        continue
    elif computer_choice not in choices or player_choice not in choices:
        print('Invalid Option')
    elif computer_choice == player_choice:
        print(f"Computer's Move: {computer_choice}")
        print('TIE')
        print(f"Player Score: {player_score}, Computer Score: {computer_score}")
    else:
        if computer_choice == 'rock':
            if player_choice == 'paper':
                result = 'Player Wins'
                player_score += 1
            elif player_choice == 'scissor':
                result = 'Computer Wins'
                computer_score += 1
        elif computer_choice == 'paper':
            if player_choice == 'rock':
                result = 'Computer Wins'
                computer_score += 1
            elif player_choice == 'scissor':
                result = 'Player Wins'
                player_score += 1
        elif computer_choice == 'scissor':
            if player_choice == 'rock':
                result = 'Player Wins'
                player_score += 1
            elif player_choice == 'paper':
                result = 'Computer Wins'
                computer_score += 1
        else:
            print('Invalid Option')

    if (result):
        print(f"Computer's Move: {computer_choice}")
        print('SHOOT!')
        print(f"Player Score: {player_score}, Computer Score: {computer_score}")
        print(result)

