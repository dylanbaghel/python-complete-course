# Exercise

import random

def flip_coin():
    return "Head" if random.randint(0, 1) else "Tail"

for i in range(20):
    print(flip_coin())