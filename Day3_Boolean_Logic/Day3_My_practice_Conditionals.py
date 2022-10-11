#a = 215
#a = int(input("Input a"))
#a = 9000
#a = 3
# # #
if True:  # after : is the code block, must be indented
    print("True")
    print("This always runs because if statement is True")
    print("Still working in if block")
#if block has ended
    print("This runs no matter what because we are outside if ")

# # # # # after we go back to our normal indentation the if block is ended
# # # #

a = 25
if a > 10: # in Python when you see : next line will be indented
#     # runs only when statement after if is True
    print("Do this when a is larger than 10")
    print(f"Still only runs when a > {a}")
#     # we can keep doing things when a > 10 here
# # #

#It is silly to use spaces manually, 
# tabs are converted by most modern IDEs to spaces for Python

if a > 10:  # in Python when you see : next line will be indented
# runs only when statement after if is True
    print("Again Do this when a is larger than 10")
    print("Indeed a is", a)
else:  # when a is <= 10
    print("Only when a is less or equal to 10")
    print("Indeed a is only", a)
#     # we could do more stuff here when a is not larger than 10

print("new if")

a = -355
# if we need more than 2 distinct paths
if a > 10:  # in Python when you see : next line will be indented
# runs only when statement after if is True
    print("Again Do this when a is larger than 10", a)
elif a < 10:
    print("ahh a is less than 10", a)
else:  # so a must be 10 no other choices you do not need to check, after all other choices are exhausted
    print("Only when a is equal to 10 since we checked other cases", a)
# we could do more stuff here when a is not larger than 10
#OUTPUT:
#ahh a is less than 10 -355
#Back to normal program flow which always runs no matter what a is
# # # # # # #
print("Back to normal program flow which always runs no matter what a is")

# # # if else elif
# a = 190
a = int(input("give me an a! "))
if a > 10:
    print("a is larger than 10")
    print("This will only happen when a > 10")
    if a >= 200: # so we can nest ifs inside another if
        print("a is truly big over  or equal 200")
    else:
        print("a is more than 10 but no more than 199")
elif a < 10:
    print("a is less than 10", a)
else: # if a == 10
    print("a is equal to 10", a)
# # #
print("This will always happen no matter the a value")

a = -100
if 2 < 3 < 8 < a:
    print(f"2 < 3 < 8 < {a} is it a True statement? ", 2 < 3 < 8 < a)
else:
    print(f"2 < 3 < 8 < {a} is it a True statement?", 2 < 3 < 8 < a)

#OUTPUT - False

