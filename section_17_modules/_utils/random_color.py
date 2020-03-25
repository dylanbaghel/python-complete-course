# random_color.py --> inside _utils folder

from random import randint, random

def generate_random_hex_color():
    valid_chars = '0123456789ABCDEF';
    color = '#'
    for i in range(1, 7):
        color += valid_chars[randint(0, len(valid_chars) - 1)]
    return color

def generate_random_rgb_color():
    color = f"rgba({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)}, {round(random(), 1)})"
    return color
