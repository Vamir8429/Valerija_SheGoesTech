my_name = "Valerija" #defining variable
print(my_name)
print(my_name + " likes gym")
print(my_name + " likes gym" * 5)

print(type(my_name)) #all variables have data types , output - <class 'str'> - string

#two main variable types - primitive and compound

my_num = 27
print(my_num)
print(type(my_num)) # integer

#id command shows in memory where your data lives - guarantee identity of your object. Unique identifier of data 

a = 27
b = 27
c = 28

print(id(a), id(b), id(c), id(my_num)) ##output 4540286000 4540286000 4540286032 4540286000

print(id(c) - id(b)) ## output 32, it means 32 bytes 

#f5 is used for debugging - slow run through program 

#It is possible to reassign variables any name 
print(a,b,c)
#underscore is used for cosmetic reasons to enter large numbers 
d = 27_000
print(d)

my_result = a + b #54 
print(my_result)

#you can change the type pf variable, but it is not recommended 

president = "Gitanas"
neighbour = "Inga"
print(my_name, president, neighbour)

print(c)
c = c + 100 #this is changing variable 
print(c) #128 
print(type(c)) #<class 'int'>

c = c + 3.145 
print(type(c)) #<class 'float'>

#i want integer instead of fload, then i do convert (type casting)
c = int(c)
print(c) #digits after comma are gone 

e = 2.714340324
e_round = round(e) #rounding function (to decimals)
print(e_round) # 3 
e_round_to_2 = round(e,2) #define rounding to decimals 
print(e_round_to_2) #output - 2.71

#import to follow guidellines of NAMING VARIABLES 
#you can use letters, numbers and underscore - no spaces, questionmarks etc 
#my_name - Python standard, follow it withing your project - CONSISTENCY
#myName - Java style, avoid it 
#numbering variables is also fine, e.g. my_name_2 
#use english names

#capital names are meant for constant, but Python does not force you to use it 
RTU = "Riga Technical University"
print(RTU)

import datetime
print("Today is", datetime.datetime.now())
print("The year is", datetime.datetime.now().year)

#my_name = input("What is your name friend? ")
#print(f"Wow that is a nice name {my_name}") 

print("Wow that is a nice name " + my_name)

#a = input("what number you want to double? ")
#double_str_a = a * 2 # a is a string so we need to convert it to an int
#print(f"Cool {a} doubled is {double_str_a}, or is it ?")

# # # #solution is to cast to the type we want
my_float = float(a) # is should do this before int cast because casting to int would lose the values
float_square = my_float**2
print(f"Cool {my_float} squared is {float_square}, or is it ?")
a = int(my_float) # so a became an integer # we could also use float(a) if we want floats
double_a = a * 2
print(f"Cool {a} doubled is {double_a}, or is it ?")


#More info on data types 
# Python built_in funcions 
# So https://docs.python.org/3/library/functions.html 
# these are all built in functions that are always available (no import needed)

# you should not name your variables the same as name of built-in functions 

# Python list reserved keywords that you are not allowed to use as variables 
# https://docs.python.org/3/reference/lexical_analysis.html#keywords


