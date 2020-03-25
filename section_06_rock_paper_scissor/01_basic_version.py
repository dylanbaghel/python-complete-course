# Rock Paper Scissor - Basic Version

print(".....rock.....")
print(".....paper....")
print(".....scissor......")

choices = ['rock', 'scissor', 'paper']
player_one_choice = input('Enter Player 1 Choice: ').lower()
player_two_choice = input("Enter Player 2 choice: ").lower()

if player_one_choice not in choices or player_two_choice not in choices:
    print('Invalid Option')
elif player_one_choice == player_two_choice:
    print('TIE')
else:
    if player_one_choice == 'rock':
        if player_two_choice == 'paper':
            print('SHOOT!')
            print('Player 2 Wins')
        elif player_two_choice == 'scissor':
            print('SHOOT!')
            print('Player 1 Wins')
    elif player_one_choice == 'paper':
        if player_two_choice == 'rock':
            print('SHOOT!')
            print('Player 1 Wins')
        elif player_two_choice == 'scissor':
            print('SHOOT!')
            print('Player 2 Wins')
    elif player_one_choice == 'scissor':
        if player_two_choice == 'rock':
            print('SHOOT!')
            print('Player 2 Wins')
        elif player_two_choice == 'paper':
            print('SHOOT!')
            print('Player 1 Wins')
    else:
        print('Invalid Option')