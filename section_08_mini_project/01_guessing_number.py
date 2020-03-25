# Mini Project - Guessing Game

import random

min = 1
max = 10
is_play = True
score = 0

while is_play:
    winning_num = random.randint(min, max)
    chances_left = 3
    while chances_left > 0:
        choice = int(input(f"Guess a number between {min} and {max}: "))
        chances_left -= 1
        if choice != winning_num:
            if (chances_left == 0):
                print(f"You Lose! -> Correct Number Was {winning_num}")
                score -= 1
                break
            if choice < winning_num:
                print(f"Too Low, try again -> Chances Left: {chances_left}")
            elif choice > winning_num:
                print(f"Too HIgh, try again -> Chances Left: {chances_left}")
        elif choice == winning_num:
            print("You Guessed It! You Won!")
            score += 1
            break
    is_play = True if input(
        'Do You Want To Play Again (yes/no): ') == 'yes' else False

print(f"Score: {score}")3
