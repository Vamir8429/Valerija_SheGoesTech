# # # you have some similar items that you want to store
# a1 = 3
# a2 = 5
# a3 = 8
# # ...
# a100 = 151
# # # # # # # There has to be a better way
# #
# # # # # # # # # What is a list after all?
# # # # # # # # # * ordered
# # # # # # # # # * collection of arbitrary objects (anything goes in)
# # # # # # # # # * nested (onion principle, Matroyshka)
# # # # # # # # # * mutable - maināmas vērtības
# # # # # # # # # * dynamic - size can change
# # # # # # # trade_off - not the most efficient as far as memory usage goes
# ## for more space efficiency there are Python libraries such as numpy
#  with ndarray structures which are based C arrays

empty_list = []  # alternative would be empty_list = list()
print(empty_list)  # we can add values later
print(len(empty_list)) #should be 0
#notice square brackets - in Python square brackets are used for list 

my_list = [5, 6, "Valdis", True, 3.65, "alus"]  # most common way of creating a 
#list using [el1, el2]
print(my_list) #[5, 6, 'Valdis', True, 3.65, 'alus']
print(type(my_list), len(my_list)) #<class 'list'> 6
#Python does not have rules for data types in a list 

#lists use the same logic of indexes
#lists are mutable
print(my_list[0])  # so list index starts at 0 for the first element #5
# # major difference with string is that lists are mutable
my_list[1] = "Mr. 50"  # lists are mutable (unlike strings) types inside 
#also will change on the run
print(my_list) #[5, 'Mr. 50', 'Valdis', True, 3.65, 'alus']
drink = my_list[-1]  # last element
print(my_list[-1], drink, my_list[5])  # again like in string we have indexes #alus alus alus
#in both directions

#photo in phone kospekt include

# # typically we do not need an index for items when looping
for el in my_list:
    print(el, "is type", type(el))
# # Pythonic way to show index is to enumerate
for i, el in enumerate(my_list):  # if we need index , default start is 0
    print(i, el, "is type", type(el))
    print(f"Item no. {i} is {el}")

#OUTPUT: 

#5 is type <class 'int'>
#Mr. 50 is type <class 'str'>
#Valdis is type <class 'str'>
#True is type <class 'bool'>
#3.65 is type <class 'float'>
#alus is type <class 'str'>
#0 5 is type <class 'int'>
#Item no. 0 is 5
#1 Mr. 50 is type <class 'str'>
#Item no. 1 is Mr. 50
#2 Valdis is type <class 'str'>
#Item no. 2 is Valdis
#3 True is type <class 'bool'>
#Item no. 3 is True
#4 3.65 is type <class 'float'>
#Item no. 4 is 3.65
#5 alus is type <class 'str'>
#Item no. 5 is alus

# # i can start index at some value
for i,el in enumerate(my_list, start=1000): # if we need index to start at some number
    print(f"Item no. {i} is {el}")

#OUTPUT: 
#Item no. 1000 is 5
#Item no. 1001 is Mr. 50
#Item no. 1002 is Valdis
#Item no. 1003 is True
#Item no. 1004 is 3.65
#Item no. 1005 is alus

list_2d = list(enumerate(my_list))
print(list_2d)

#OUTPUT: 

#[(0, 5), (1, 'Mr. 50'), (2, 'Valdis'), (3, True), (4, 3.65), (5, 'alus')]

numbers = list(range(10)) # range is not a list it used to be in Python 2.7, it is ready on demand
print(numbers)

#OUTPUT - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(len(my_list))
# for i in range(len(my_list)): # this way is not encouraged, this is too C like, no need for this style
#     print(f"Item no. {i} is {my_list[i]}")

drinks = ["water", "juice", "coffee", "tea", "milk", "beer"]
# idioms
for drink in drinks:  # list in plural item in singular
    print(drink)

#OUTPUT: 
#water
#juice
#coffee
#tea
#milk
#beer

# List slicing - we can use it to get a part of the list
print(my_list[:3]) # so we only print the first 3 elements from the list
print(my_list[-2:]) # last two
print(my_list[1:4]) # from the second to the fourth, fifth is not included
print( my_list[1:-1]) # from the second to the last but one
print(my_list[::2]) # jumping over every 2nd one
my_numbers = list(range(100,200,10)) # no 0 lidz 9, also shows how to create a list from another sequence like object
print(my_numbers)
print(numbers)
print(numbers[::2])  # evens starting with 0, since we jump to every 2nd one
print(numbers[1::2])  # so odd numbers here
print(my_numbers[::2]) # even starting with 0, 2, 4
print(my_numbers[1::2]) # all odd indexed numbers, index 1, 3, 5, 7
# # # # print(my_list[1::2]) # start with 2nd element and then take every 2nd element
# # print(my_list[-1], my_list[len(my_list)-1]) # last element, we use the short syntax
print(my_numbers[::-1])
print(my_list[::-1])
print(numbers[::-1])

#[5, 'Mr. 50', 'Valdis']
#[3.65, 'alus']
#['Mr. 50', 'Valdis', True]
#['Mr. 50', 'Valdis', True, 3.65]
#[5, 'Valdis', 3.65]
#[100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#[0, 2, 4, 6, 8]
#[1, 3, 5, 7, 9]
#[100, 120, 140, 160, 180]
#[110, 130, 150, 170, 190]
#[190, 180, 170, 160, 150, 140, 130, 120, 110, 100]
#['alus', 3.65, True, 'Valdis', 'Mr. 50', 5]
#[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(reversed(numbers)) # this we would use when we do not need the list completely for looping
# # why would you use such a construction
# # because you do not want to create a new list in memory, you want to use the original
for n in reversed(numbers):  # this is more efficient than numbers[::-1] because we do not create a new list in memory
    print(n)
# print(list(reversed(numbers)))
my_reversed_numbers = my_numbers[::-1]
print(my_reversed_numbers)

#<list_reverseiterator object at 0x10c663f70>
#9
#8
#7
#6
#5
#4
#3
#2
#1
#0
#[190, 180, 170, 160, 150, 140, 130, 120, 110, 100]

print("END OF EXAMPLE")

food = "kartupelis"
print(food)
food_chars = list(food) # so type casing just like str, int, float, bool etc
# list will work with any sequence type - and str is a sequence type
print(food_chars)
print("OLD and TIRED", food_chars[5])
food_chars[5] = "m"  # so replacing the 6th elemen - in this case a letter p with m
print("NEW and FRESH", food_chars[5])
print(food_chars)
maybe_food = str(food_chars) # not quite what we want, but it is a string
print(maybe_food) # just a string of what printing a list would look like
# so maybe_food is a string, but it is not a list anymore
food_again = "".join(food_chars) # "" shows what we are putting between each character, in this case nothing
print(food_again)
food_again_with_space = " ".join(food_chars) # "" shows what we are putting between each character
print(food_again_with_space)
food_again_with_smile = "**😁**".join(food_chars) # "" shows what we are putting between each character
print(food_again_with_smile)
small_list = ["Valdis", "likes", "beer"]
separator = "==="
new_text = separator.join(small_list)
print(new_text)
# num_string = "||".join(numbers) # we will need to convert numbers to theri str representation
# print(num_string)

#kartupelis
#['k', 'a', 'r', 't', 'u', 'p', 'e', 'l', 'i', 's']
#OLD and TIRED p
#NEW and FRESH m
#['k', 'a', 'r', 't', 'u', 'm', 'e', 'l', 'i', 's']
#['k', 'a', 'r', 't', 'u', 'm', 'e', 'l', 'i', 's']
#kartumelis
#k a r t u m e l i s
#k**😁**a**😁**r**😁**t**😁**u**😁**m**😁**e**😁**l**😁**i**😁**s
#Valdis===likes===beer

print("END OF EXAMPLE")

# # # print(list("kartupelis")) # can create a list out of string
print("kartupelis".split("p")) # i could split string by something
sentence = "A quick brown fox jumped over a sleeping dog"
print(sentence)  # string
words = sentence.split(" ")  # we split by some character in this case whitespace
print(words) # list with words
#
# sentence_with_exclams = ".!.".join(words)
# print(sentence_with_exclams)
# # # # # # # # # how to check for existance in list
print(my_list)
print("3.65 is in my list?", 3.65 in my_list)
# print(66 in my_list)
print("Valdis" in my_list)
print(my_list[2]) # Valdis
print("al" in "Valdis", "al" in my_list[2])
print("al" in my_list)  # this is false,because in needs a exact match, to get partial we need to go deeper
# # # # # # # # # # # iterate over items
# print("*"*20)
# # for it in my_list:
# #     print(it)
# #

#['kartu', 'elis']
#A quick brown fox jumped over a sleeping dog
#['A', 'quick', 'brown', 'fox', 'jumped', 'over', 'a', 'sleeping', 'dog']
#[5, 'Mr. 50', 'Valdis', True, 3.65, 'alus']
#3.65 is in my list? True
#True
#Valdis
#True True
#False

print("END OF EXAMPLE")

needle = "al" # what we want to find in our list
for item in my_list:
    print("Checking ", item)
    if type(item) == str and needle in item: # not all types have in operator
        print(f"Found {needle=} in {item=}") # python 3.8 and up, good for debuggin
        print(f"Found needle={needle} in item={item}") # for python 3.7

#Checking  5
##Checking  Mr. 50
#Checking  Valdis
#Found needle='al' in item='Valdis'
#Found needle=al in item=Valdis
#Checking  True
#Checking  3.65
#Checking  alus
#Found needle='al' in item='alus'
#Found needle=al in item=alus

print("END OF EXAMPLE")

#ADDING ITEM to the list 
#so append is IN PLACE method for a list, meaning it modifies the list it comes with, 
# you do not need to assign a new variable
my_list.append("Bauskas alus") # adds "Bauskas alus" at the end of my_list
my_list.append("Valmiermuižas alus")  # IN PLACE methods, means we modify the list
print(my_list)

#[5, 'Mr. 50', 'Valdis', True, 3.65, 'alus', 'Bauskas alus', 'Valmiermuižas alus']

#so whenever you use some method check whether it is IN PLACE or OUT OF PLACE

print("END OF EXAMPLE")

# # # # # # # # # example how to filter something
find_list = [] # so we have an empty list in beginning
needle = "al"
for item in my_list: # i can reuse item in the loop
    # if needle in item: will not work because we have non strings in list
    if type(item) == str and needle in item:
        print(f"Found {needle=} in {item=}")
        find_list.append(item)
print(f"{needle=} found in {find_list=}")
# # # # # # # # # ps the above could be done simpler with list comprehension

#Found needle='al' in item='Valdis'
#Found needle='al' in item='alus'
#Found needle='al' in item='Bauskas alus'
#Found needle='al' in item='Valmiermuižas alus'
#needle='al' found in find_list=['Valdis', 'alus', 'Bauskas alus', 'Valmiermuižas alus']

print("END OF EXAMPLE")

new_list = my_list + ["Kalējs", "Audējs"] # OUT OF PLACE addition, my_list is not modified
print(len(new_list), len(my_list))
print(my_list)
print(new_list)

new_list += ["Malējs", "Salīgais"] # shorthand for new_list = new_list + [new items ] so flattened
print(new_list)
new_list.append(["Svarīgais", "Mazais"]) #notice append added a list a s nested
print(new_list) # notice that we have a list in the list
print(new_list[-1])
print(new_list[-1][-1], new_list[-1][1]) # in this case for size 2 1 and -1 give same results
new_list.extend(["Fantastiskais", "Lapsa"]) # very similar to += IN PLACE
print(new_list)

#10 8
#[5, 'Mr. 50', 'Valdis', True, 3.65, 'alus', 'Bauskas alus', 'Valmiermuižas alus']
#[5, 'Mr. 50', 'Valdis', True, 3.65, 'alus', 'Bauskas alus', 'Valmiermuižas alus', 'Kalējs', 'Audējs']
#[5, 'Mr. 50', 'Valdis', True, 3.65, 'alus', 'Bauskas alus', 'Valmiermuižas alus', 'Kalējs', 'Audējs', 'Malējs', 'Salīgais']
#[5, 'Mr. 50', 'Valdis', True, 3.65, 'alus', 'Bauskas alus', 'Valmiermuižas alus', 'Kalējs', 'Audējs', 'Malējs', 'Salīgais', ['Svarīgais', 'Mazais']]
#['Svarīgais', 'Mazais']
#Mazais Mazais
#[5, 'Mr. 50', 'Valdis', True, 3.65, 'alus', 'Bauskas alus', 'Valmiermuižas alus', 'Kalējs', 'Audējs', 'Malējs', 'Salīgais', ['Svarīgais', 'Mazais'], 'Fantastiskais', 'Lapsa']

print("END OF EXAMPLE")

