import random

def single_die():
    return random.randint(1,6)

def dice_roll(dice_count):
    out = 0
    for _ in range(dice_count):
        out += single_die()
    return out

def dice_rolls(dice_count, rolls_count):
    out = []
    for _ in range(rolls_count):
        out.append(dice_roll(dice_count))
    return out

print(dice_rolls(2,100))    