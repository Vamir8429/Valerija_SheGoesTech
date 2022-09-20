# 1a. Average value

# Write a program that prompts the user to enter numbers (float).
# The program shows the average value of all entered numbers after each entry.

# PS. 1a can do without a list

# 1b. The program shows both the average value of the numbers and ALL the numbers entered
# PS Exit the program  by entering "q"

# 1c The program does not show all the numbers entered but only TOP3 and BOTTOM3 
# and of course still average.

list_numbers = []

while True:
    user_input = float(input(
        "Please enter numbers(separated by comma) or 'q' to quit: "))
    if user_input == "q":
        print("You quit")
        break

    else:
        list_numbers.append(float(user_input))
        sorted_number_list = sorted(list_numbers) 
        # if we did not need original order
        # then we could have used list_numbers.sort() instead
        average_calculated = sum(list_numbers) / len(list_numbers)
        print(
            f"Numbers you entered are: {list_numbers} , average is: {average_calculated}")

        print(f"Top 3 values you enetered are: {sorted_number_list[-3:]}")
        print(f"Bottom 3 values you entered are: {sorted_number_list[:3]}")