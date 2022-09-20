# 1a. Average value

# Write a program that prompts the user to enter numbers (float).
# The program shows the average value of all entered numbers after each entry.

# PS. 1a can do without a list

# 1b. The program shows both the average value of the numbers and ALL the numbers entered
# PS Exit the program  by entering "q"

# 1c The program does not show all the numbers entered but only TOP3 and BOTTOM3 
# and of course still average.

my_list = []
user_input = int(input("Please enter couple of numbers:"))
number_list = user_input.split(" ")
while True:
    if user_input == "q":
        print("You exited the program. Start again! ")
        break
    else: 
        my_list.append(number_list)
        print(f"All numbers entered by user: , {my_list}")
        print(f"Average of all entered numbers: , {my_list}\nAverage is {sum(my_list) / len(my_list):.2f}")
        print(f"BOTTOM 3 {sorted(my_list)[:3]}")
        print(f"TOP 3 {sorted(my_list)[-3]}")

#PHOTO - NORMAL SOLUTION