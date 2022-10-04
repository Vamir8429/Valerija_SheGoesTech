needle = "roads"  # what i want to find
# # # # # # # # with open('Diena_12_Faili/frost.txt', encoding="utf-8") as f:  # create a file object
with open('frost.txt', encoding="utf-8") as f:  # create a file object
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