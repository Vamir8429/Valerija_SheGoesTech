# 2. Xmas Bonus

# The company has promised a Christmas bonus in the amount of 15% of the monthly salary for EVERY year of 
# service over 2 years.

# Task. Ask the user for the amount of the monthly salary and the number of years worked.

# Calculate the bonus.

# Example1: 5 years of experience, 1000 Euro salary, the bonus will be 450 Euro.

# Example2: 1.5 years of experience, 1500 Euro salary, no bonus(0)

s = float(input("What is your monthly salary? t!"))
y = int(input("How many years you have worked at this company? y!"))
if y >= 2:
    print(int(s * 0.15 * y))
else:
    print("Unfortunately, no bonus for you :(")