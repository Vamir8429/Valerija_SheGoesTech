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