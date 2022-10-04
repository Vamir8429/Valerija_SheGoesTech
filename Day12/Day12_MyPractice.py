import os
import string
import datetime as dt
from pathlib import Path

#my_path = Path("frost.txt")  # so this will create correct name on all 3 OSes
#print(my_path)

needle = "roads"  # what i want to find
# # # # # # # # with open('Diena_12_Faili/frost.txt', encoding="utf-8") as f:  # create a file object
with open("Day12/frost.txt", encoding="utf-8") as f:  # create a file object
    # filtered_lines = [line for line in f if needle in line]
    #     # i cant do second loop without seek
    #     # same as above list comprehension
    # for more complex filtering
    filtered_lines = []
    for line in f:
        if needle in line:
            filtered_lines.append(line)
#
print(filtered_lines)

#OUTPUT
#['Two roads diverged in a yellow wood,\n', 'Two roads diverged in a wood, and I—\n']