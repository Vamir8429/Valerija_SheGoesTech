#Forloops 
# # for loops are for definite iteration

for num in range(5):  # range is sort of half ready number sequence , 
#num is a variable created for each iteration
#     # range starts with 0 and ends with 4
    print(num)
    print("Hello there!")
    print("Number is", num)
print("out of loop", num)
# # # # so range takes range(start(default 0), end(not included), step)

#OUTPUT 

#0
#Hello there!
#Number is 0
#1
#Hello there!
#Number is 1
#2
#Hello there!
#Number is 2
#3
#Hello there!
#Number is 3
#4
#Hello there!
#Number is 4
#out of loop 4

#So many things in Python just like most languages start with 0 and go UNTIL something

for i in range(1, 11): # so careful of off-by-one errors, remember range will stop at 10 not 11 here!
    print(f"I like this {i} better")
#it runs from 1 to 10

# # we can also iterate over strings
my_name = "Valerija M"
# # # my_name = "Kaķis Ņauva"
for c in my_name: # c could be also char, or my_c, c is just shorter
    print("Letter ", c)
    print(f"Letter {c} Unicode is {ord(c)}")

# range with 2 parameters we have start inclusive and until end exclusive
for n in range(20,25):  # we loop until 24
    print(n)

#so range also has an optional step parameter
#only restriction to range parameters is that they have to be 
# integers (not floats) there are specific libraries for float ranges

start = 10
end = 37
step = 4
early_break = 27
for my_num in range(start,end+1,step): # i can add step to range
    print(my_num)
    if my_num > early_break:
        print(f"Reached our early break threshold {early_break}")
        break

#OUTPUT
#10
#14
#18
#22
#26
#30
#Reached our early break threshold 27


#SO you can put loops inside loops (for and/or while loops)
#careful, because nested loops can take more time 

# we can nest loops

big_total = 0
even_number_count = 0
for i in range(1,5): # outer loop
    for j in range(1, 3):  #inner loop
        result = i * j
        print(f"{i}x{j}={result}")
        big_total += result
        if result % 2 == 0:
            print("oh even number", result)
            even_number_count += 1
#
print("Total is", big_total)
print("Even number count is", even_number_count)

#OUTPUT 
#1x1=1
#1x2=2
#oh even number 2
#2x1=2
#oh even number 2
#2x2=4
#oh even number 4
#3x1=3
#3x2=6
#oh even number 6
#4x1=4
#oh even number 4
#4x2=8
#oh even number 8
#Total is 30
#Even number count is 6

for n in range(1,21):  # from 1 until 20
    if n%2 == 0: # even numbers have no reminder when divided by 2
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

print("Another example") 

print(" "*10+"*"*6)
# # #same as above
for _ in range(10):
    print(" ", end="")
for _ in range(6):
    print("*", end="")
print() # prints new line

#OUTPUT: 
# ******
# ******