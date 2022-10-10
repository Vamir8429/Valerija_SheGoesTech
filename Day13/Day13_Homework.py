# TODO
# put the imports first

import random
from collections import Counter
import matplotlib.pyplot as plt

# create a function that returns a list of random dice throws
# it should have two parameters
# - number of dice in each throw, default 4
# - number of throws, default 100

def dice_throw(dice, throw):
    dice_list = [random.randint(1, 4) for _ in range(0,throw)]
    print(dice_list)

dice_throw(3,10) #[3, 2, 1, 3, 3, 2, 1, 2, 3, 1]

# even better would be a another function to which you give the list of dice throws and it 
# plots the histogram
# this function would have two parameters
# - the list of dice throws - no default
# - the name of the file to save the plot to - default - empty string
# if the file name is empty string, the plot should be shown on the screen

# use the first function to create a list of 1000 dice throws with 6 dice in each throw
# pass the result to 2nd function to plot the histogram and save it to a file

def dice_throw2(dice, throw):
    dice_list = [random.randint(1, 4) for _ in range(0,throw)]
    print(dice_list)
    #plot a histogram of the list
    plt.hist(dice_list,bins=range(dice+1,throw+1))
    plt.xlabel('Throw')
    plt.ylabel('Dice')
    plt.title('Histogram of Dice Throws')
    plt.show()

dice_throw2(3,10)

# BONUS: file name should have current date and time in it

# ideally you would then run them from main guard
# which means this file would be a module, that can be imported
