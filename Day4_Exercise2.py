#  2. Christmas tree 
# # Ask user to enter the height of the tree 
# # Then Print the tree: Ex. height == 3 
#  The printout would be: 
#   * 
# # ***** 
# Note: remember that several symbols 
# can be printed at once, for example: print ("" * 10 + "*" * 6)

height = int(input("Enter the height of the tree "))
for i in range(1, height+1):
    print("*" * i)
i = i + 1
print("Here you go")

#correct solution:

c_symbol = "*"
height = 0
while True:
    a = input("Enter the height of the tree (positive number) or q for exit: ")
    if a == "q":
        break

    try:
        height = int(a)
    except ValueError:
        print("Please enter a number")
        continue

    for i in range(height):
        # print(c_symbol * (2 * i - 1))
        print(' ' * (height - i - 1) + c_symbol * (2 * i + 1))