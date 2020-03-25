from pyfiglet import figlet_format
from termcolor import colored

allowed_colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')

msg = input('What Would You Like To Print? ')

while True:
    try:
        color = input('What Color: ')
        if (color not in allowed_colors):
            raise ValueError()
        ascii_art = figlet_format(msg)
        colored_ascii = colored(ascii_art, color=color)
        print(colored_ascii)
    except ValueError:
        print('Invalid Color')
    else:
        break
