# TODO
# put the imports first

import random
from collections import Counter
import matplotlib.pyplot as plt

#    for _ in range(rolls_count):
#        out.append(dice_roll(dice_count))
#    return out

# create a function that returns a list of random dice throws
# it should have two parameters
# - number of dice in each throw, default 4
# - number of throws, default 100

def single_throw():
    return random.randint(1,6)

def dice_throw(dice_count):
    out = 0
    for _ in range(dice_count):
        out += single_throw()
    return out

def dice_rolls(dice_count, throws_count):
    my_list = []
    for _ in range(throws_count):
        my_list.append(dice_throw(dice_count))
    print(my_list)

dice_rolls(3,20)

# even better would be a another function to which you give the list of dice throws and it 
# plots the histogram
# this function would have two parameters
# - the list of dice throws - no default
# - the name of the file to save the plot to - default - empty string
# if the file name is empty string, the plot should be shown on the screen

# use the first function to create a list of 1000 dice throws with 6 dice in each throw
# pass the result to 2nd function to plot the histogram and save it to a file
# BONUS: file name should have current date and time in it

# ideally you would then run them from main guard
# which means this file would be a module, that can be imported
