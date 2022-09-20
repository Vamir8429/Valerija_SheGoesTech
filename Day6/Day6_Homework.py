#Homework exercise: 

# Find and output the first 20 
# (even better option to choose how many first primes we want) 
# prime numbers in the form of a list i.e. [2,3,5,7,11, ...
# so remember we already know how to find a single prime number 
# from previous exercise
# https://github.com/ValRCS/Python_SheGoesTech_22/blob/main/Day_4_Loops/day4_exercise_3.py


n = 100
primes = []
for i in range(2, n+1):
	for j in range(2, int(i ** 0.5) + 1):
 		if i%j == 0:
 			break
	else:
		primes.append(i)
###print(primes)
print(primes[:20], "-First 20 prime numbers")