# Exercise
# read text from  sherlock_holmes_adventures.txt

# 1a -> write the function file_line_len(fpath), which returns the number of lines in the file
# check file_line_len("sherlock_holmes_adventures.txt") -> 12305

# 1b -> write the function get_text_lines(fpath), which returns a 
# list with only those lines that contain text.
# So we want to avoid/filter out those lines that contain whitespace
# PS preferably use encoding = "utf-8" when reading 

# 1c -> write the function save_lines(destpath, lines)
# This function will store all lines into destpath file 

# 1d -> call save_lines with destpath being "pure_sherlock.txt" and lines being the text lines we cleaned from 1b

# 1e -> write the function clean_punkts(srcpath, destpath)
# function will open the srcpath file, 
# clear it from https://docs.python.org/3/library/string.html#string.punctuation

# then function will save the cleaned text into destpath
# clean_punkts("pure_sherlock.txt", "clean_sherlock.txt")

# 1f -> write the function get_word_usage(srcpath, destpath)
# The function opens the file and finds the most frequently used words
# recommendation to use Counter module!
# assume that the words are separated by either whitespace or newline 
# (the good old split will come in handy)
# the saved list of words and frequency should be saved in destpath in the following form:
# word, count
# un, 3423
# es, 3242

# in effect you will be saving in standard csv format - https://docs.python.org/3/library/csv.html
# you can use csv module for this, but it is not necessary

import os
import string
import datetime
from pathlib import Path

with open("Day12/sherlock_holmes_adventures.txt") as fstream:
    text = fstream.read()

#1A: function to find lenght of file 
def file_line_len(file_name):
    file_len = 0
    with open(file_name, encoding="UTF-8") as f:
        for _ in f:  # will work even on large files
            file_len += 1
    return file_len

result = file_line_len("Day12/sherlock_holmes_adventures.txt")
print(result) #12304

#1B: write the function get_text_lines(fpath), which returns a 
# list with only those lines that contain text.

def get_text_lines(fpath):
    with open(fpath,encoding='utf-8') as f:
        # filter out lines that contain only whitespace
        # whitespace is defined by string.whitespace
        # https://docs.python.org/3/library/string.html#string.whitespace
        # whitespace is \n, \t, \r, \v, \f, ' '
        lines = [line.strip() for line in f if line.strip()]
        # lines = [line for line in lines if len(line.strip()) > 0]
    return lines

# 1c -> write the function save_lines(destpath, lines)
# This function will store all lines into destpath file 

def save_lines(destpath, lines, sep='\n', encoding='utf-8'):
    with open(destpath, "w", encoding=encoding) as f:
        for line in lines:
            f.write(line + sep)

# 1d -> call save_lines with destpath being "pure_sherlock.txt" 
# and lines being the text lines we cleaned from 1b

#poem_lines = get_text_lines("Day12/sherlock_holmes_adventures.txt")
#save_lines("Day12/pure_sherlock.txt", poem_lines)

# let's add a new line at the end of each line
# 
#save_lines("pure_sherlock_b.txt", text_lines)
# if we ant to add a new line at the end of each line
#text_lines_with_newlines = [line + '\n' for line in text_lines]
# then we pass empty string as a separator
#save_lines("pure_sherlock.txt", text_lines_with_newlines, sep="")


#1E:

import string
def clean_punkts(srcpath, destpath):
    with open(srcpath, encoding="utf-8") as fin, open(destpath, mode="w", encoding="utf-8") as fout:
        for line in fin:
            for character in line:
                if character in string.punctuation: # you could skip this if and just use replace
                    line = line.replace(character, '')                    
            fout.write(line)

#srcpath='Day12/pure_sherlock.txt'
#destpath='Day12/clean_sherlock.txt'
#clean_punkts(srcpath, destpath)

# 1f -> write the function get_word_usage(srcpath, destpath)
# The function opens the file and finds the most frequently used words
# recommendation to use Counter module!
# assume that the words are separated by either whitespace or newline 
# (the good old split will come in handy)
# the saved list of words and frequency should be saved in destpath in the following form:
# word, count
# un, 3423
# es, 3242

# in effect you will be saving in standard csv format - https://docs.python.org/3/library/csv.html
# you can use csv module for this, but it is not necessary

from collections import Counter

def get_word_usage(srcpath, destpath):
            with open(srcpath, encoding="utf-8") as fin, open(destpath, mode="w", encoding="utf-8") as f:
                word_list = tuple(fin.split())
                word_count = Counter(word_list)
                f.write(word_count)

srcpath='Day12/pure_sherlock.txt'
destpath='Day12/count_sherlock.txt'
get_word_usage(srcpath, destpath)