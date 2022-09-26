# # 1. What's the frequency?

# Write a function: get_char_count(text) that receives a 
# string and returns a dictionary with the number of single letter counts.

# get_char_count("hubba bubba") -> {'h': 1, 'u': 2, 'b': 5, 'a': 2, ' ': 1} 

# # dictionary sequence doesn't matter and the whole alphabet doesn't 
# have to be included

#  There may also be a solution with Counter from standard Python 
# library but this is definitely not necessary, although it is very elegant smile

from collections import Counter

def get_char_count(text):
    my_output = {}
    for i in text:
        if i in my_output: 
            my_output[i] += 1
        else:
            my_output[i] = 1
    return my_output

print(get_char_count("Hellolove"))

