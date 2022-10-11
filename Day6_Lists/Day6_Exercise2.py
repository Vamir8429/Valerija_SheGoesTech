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

number_1 = int(input("Enter the beginning number: "))
number_2 = int(input("Enter the end number: "))
print(number_1, "-This is my beginning number")
print(number_2, "-This is my end number")
my_list = list(range(number_1,number_2+1))
cubes = []
for num in my_list:
    cubes_single = num**3
    cubes.append(cubes_single)
    print(f"{num} cubed: {cubes_single}")
print(cubes, "-All cubes!")

#OUTPUT: 
#Enter the beginning number: 2
#Enter the end number: 5
#2 -This is my beginning number
#5 -This is my end number
#2 cubed: 8
#3 cubed: 27
#4 cubed: 64
#5 cubed: 125
#[8, 27, 64, 125] -All cubes!