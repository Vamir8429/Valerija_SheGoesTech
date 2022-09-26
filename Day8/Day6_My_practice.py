tel = {'valdis': 2640, 'līga': 2911}  # create dict with 2 key-value pairs
print(tel)

tel['maija'] = 2653  # i add a new key-value pair to the dictionary or overwrite the old one
print(tel)

print(tel['valdis'])  # this lookup will be very fast O(1) even with huge dictionary
# #
key = "maija"
print(tel[key])  # get value by key

# # # if I have many phones well, then I have options, how about a list?
tel['valdis'] = [2640, 1188, 911]  # setting value to a list
print(tel)

may_phone = tel[key] # we can always save values/reference in a new variable
print(may_phone) # once it is out no relation to dictionary

print(tel.keys(), type(tel.keys()))
key_list = list(tel.keys()) # so i can create a list of dictionary keys
print(key_list)  # these values are not related to dictionary keys anymore

print(tel.keys(), type(tel.keys()))
key_list = list(tel.keys()) # so i can create a list of dictionary keys
print(key_list)  # these values are not related to dictionary keys anymore
# #
# # # # # similarly I can extract values from a dictionary
print(tel.values(), type(tel.values()))
value_list = list(tel.values())
print(value_list)
# #
key_list.append("rūta")
value_list.append(1008)
# # of course I could have just added tel["rūta"] = 1008 directly like in the above examples
#
print(key_list)
print(value_list)

new_dict = dict(zip(key_list,value_list))
print(new_dict)

print('valdis' in tel) # so i check for key in my dictionary very quickly
print('Valdis' in tel) # case sensitive so False
print('joker' in tel)

print(tel.get("valdis"))  # so it is just like tel["valdis"] but with error handling
print(tel.get("NoSuchKey"))  # so if no key exists I get None back
print(tel.get("NoSuchKey", "Sorry no such key found"))  # i can also add a default value
print(tel.get("valdis", "Sorry no such key found"))  # i can also add a default value

print(1001 in tel.values()) # going through values will be slow, unlike keys

tel[""] = "Should not work" # it but turns out it does
print(tel.keys())
print(tel[""])
tel["empty_string"]= "" # this is normal
tel["none_value"] = None # this is normal to store unknown values
print(tel)

tel["inner_dict"] = {"first phone":22222, "second phone" : 34322}  #so we can store dictionaries inside dictionaries
print(tel)

my_key = "valdis"
#my_key = "notarealkey"
if my_key in tel:
    print("key:", my_key, "value:", tel[my_key])
else:
    print("Couldn't find this key", my_key)


for key in tel: # so we can iterate over all keys in a dictionary
    print("key:", key, "value:", tel[key]) # no need for get since we are guaranteed key
    # just remember NOT to modify dictionary size(delete or add) when looping over it
# #

print("NEW EXAMPLE")

for key,value in tel.copy().items(): # i could have gone through backup as well
    if type(value) is not int or value < 2_000:
        del tel[key] # this changes the size of original dictionary
        # tel[key+"BIGGIE"] = value*10 # i can add a new key too if i want
print(tel)  # original is changed
food = "kartupelis"
numbers = list(range(10))
letter_dict = dict(zip(numbers, food))
print(letter_dict)
print(letter_dict[3]) # here list would better since we have numbers in order
number_dict = dict(zip(food, numbers))
print(number_dict)

print("NEW EXAMPLE")

my_counter = {key:0 for key in food}  # set default value to 0
print(my_counter)
#
# # so how to adjust values in dictionary
blank_dict = {}
numbers = list(range(12))
for n in numbers: # we loop through list and do something to dictionary
    if n > 4:
        if "over4" in blank_dict:  #there is an option called setdefault which is a bit shorter
            blank_dict["over4"] += 1 #we increase the count by 1
        else:
            blank_dict["over4"] = 1   # initialize the value to 1
    else: # 4 or less
        if "4orless" in blank_dict:
            blank_dict["4orless"] += 1
        else:
            blank_dict["4orless"] = 1

print(blank_dict)

print("NEW EXAMPLE")

for c in "my name is Valdis":
    if c.isalpha():
        print("This is a letter", c)
    else:
        print("Not a letter", c)


print("New example")

value_to_find = 2911
new_dict = {} # empty dict to hold both key and value
names_with_1001 = [] # empty list to hold just the names/keys, not really needed
# #
# # # # so filtering for values in a dictionary
for key, value in tel.items():
    if value == value_to_find:
        print(f"Match for {value} found! The key to be added is {key}")
        new_dict[key] = value # setdefault would also work
        names_with_1001.append(key) # saving just the names in a list
# #
print(new_dict)
print(names_with_1001, list(new_dict.keys()))

