# # 2. Cubes

# The user enters the beginning (integer) and end number.
# The output is the entered numbers and their cubes
# For example: inputs 2 and 5 (two inputs)

# Output

# 2 cubed: 8
# 3 cubed: 27
# 4 cubed: 64
# 5 cubed: 125

# All cubes: [8,27,64,125]
# PS could theoretically do without a list, but with a list it will be more convenient

input_1 = int(input("Please enter first number: "))
input_2 = int(input("Please enter last number: "))
if input_1 < input_2:
    cubed_list = [n**3 for n in range(input_1, input_2+1)]
    print(cubed_list)
else:
    print("Invalid input")

#Please enter first number: 2
#Please enter last number: 5
#[8, 27, 64, 125]