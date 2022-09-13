# # 1. FizzBuzz 

# Print a string 1,2,3,4, Fizz, 6, Buzz, 8, ..... 34, FizzBuzz, 
# 36, .... to 97, Buzz, 99, Fizz 

# So if number divided by 5 then Fizz If divided by 7 then Buzz,
#  If divided by 5 AND 7 then FizzBuzz otherwise the same number

#  Note: such a task became popular as the first task to ask to determine 
#  whether a person knows about programming at all smile


for n in range(1,100): #from 1 to 99
    if n % 5 == 0:
        print("Fizz", end=",")
    elif n % 7 == 0:
        print("Buzz", end=",")
    elif n % 5 == 0 and n % 7 == 0:
        print("FizzBuzz", end=",")
    else:
        print(n, end=",")

#OUTPUT: 
#1,2,3,4,Fizz,6,Buzz,8,9,Fizz,11,12,13,Buzz,Fizz,16,17,18,19,Fizz,Buzz,
# 22,23,24,Fizz,26,27,Buzz,29,Fizz,31,32,33,34,Fizz,36,37,38,39,Fizz,
# 41,Buzz,43,44,Fizz,46,47,48,Buzz,Fizz,51,52,53,54,Fizz,Buzz,57,58,59,
# Fizz,61,62,Buzz,64,Fizz,66,67,68,69,Fizz,71,72,73,74,Fizz,76,Buzz,78,79,
# Fizz,81,82,83,Buzz,Fizz,86,87,88,89,Fizz,Buzz,92,93,94,Fizz,96,97,Buzz,99,%
