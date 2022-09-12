is_raining = False  #this is boolean operator 
is_sunny = True
is_summer = False

#False is usually 0, true - 1 

print(is_raining, is_sunny)
print(type(is_raining), type(is_sunny), type(is_summer))  #<class 'bool'> <class 'bool'> <class 'bool'>
print(2 * 2 == 4) # notice  double == , this is comparison this is not assignment!
#output = True

is_math_correct = 2 * 2 == 4  # we go from right to left, parenthesis are not required
print(is_math_correct) #True 

a = 2
b = 4
print(a * a == b, a * a == 4, a * a == 5)  # more common, True True False 
print(2 == 2.0)  # two types but should be true, True 

print(1 == True, True == 1, False == 0, 0 == False)  # True is represented by 1, we should actually use is to compare with False and True
print(1 == True, True == 1, False == 0, 0 == False)  # True is represented by 1, we should actually use is to compare with False and True
print(True+True+True+False) # so 3 because this is just regular math with 1 and 0

print("" == False)  # empty string is not the same as False but it will be used similarly in logical operations
print("" == '')  # True because it is same empty string
my_name = "Valerija"
print(my_name == my_name, my_name == "Valerija", my_name == "Volerija") #True, True, False
print("Valerija" == 27) #False, because they are different types 

# # # # inequality
print(a,b) #2,4
print(a != b)  # if they are inequal then != will give True
print(2 != 2)  # this is a False statement because 2 is in fact equal to 2
is_not_equal = a * 2 != b  # a false statement because a * 2 is equal to 4
print(is_not_equal) #False 

# != it is inequality comparison 

# #
# # # # greater >
print(2 > 3, 3 > 2, 9001 > 9000) #False, True, True 
print(a * a > 3, a * a > b, a * a > 5, a * a > b * 15) #True, False, False, False
b = 10
print(a * a > 3, a * a > b, a * a > 5, a * a > b * 15) #True, False, False, False 
print(True > False)  # if True is 1 and False is 0 then this should be True :) #True 

# # # # we can compare other data types
print("Voldemars" > "Valdis")  # gives us True but why?
# Why? because o is further than a in the alphabet -alphabetical ordering 

print(ord("V"), ord("a"), ord("o"), ord("ā"), ord("😀"))  #86 97 111 257 128512
# we can get Unicode codes for characters
print(chr(86), chr(97), chr(257), chr(8000), chr(128512))  #V a ā ὀ 😀
# i can print from codes the symbols

#Indeed, comparing Strings uses tiebreaks, 
#if V is first letter for both strings, then it check next letter and so on

# # # if we need by length - we can measure length of sequences , strings and many other types
print(len("Voldemārs") > len("Valdis"))  #True 
print(len("Voldemārs")) #9
print(len("Valdis")) #6

# # # less than <
print(a,b) #2, 10
print(2 < 3, 3 < 3, a < b, b < a) #True, False, True, False
# # #
# # # # less or equal
print(2 <= 3, 3 <= 3, 3 <= 4, 5 <= 3) #True, True, True, False
print(a <= 14, a <= 15, b <= 16) #True, True, True
# # #
# # # # gt greater or equal
print(2 >= 3, 3 >= 3, 4 >= 3, a * 2 >= b * 3) #Falsem True, True, False 
# # #

c = 50
print(a,b,c,1000) #2, 10, 50, 1000
print(a < b < c < 1000)  # a is still 15 here so this will be false. True 
a = 8

# # we can compare more than two at once
print(a,b,c,1000) #8, 10, 50, 1000
print(a < b < c < 1000)  # four values at once, True 
print(a < -50 < b < c < 1000)  # false because first operation shortcircuits to False, False
# # #

# # # # is compares actual memory address
# # # # used less
print(a is b)  # really it is id(a) == id(b) - False
print(2 is 2)  # should not really use instead use == AVOID! - True 

print(2*2 == 4 is True) # use to compare something with True or False. TRUE
# # # # we use it when we need to see if both variables point to same object
# # # is can be handy for finding whether you have same shopping cart
# # or you have two different shopping carts with same items - just an analogy
print(a,b,c) #8, 10, 50
print(a + b == c - 32, a + b == c + 1 - 32) #True, False
print("All Done") #All done 

