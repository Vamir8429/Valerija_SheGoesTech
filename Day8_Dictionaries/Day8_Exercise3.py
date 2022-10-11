# # 3. Dictionary cleaner


# 3a. Write clean_dict_value(d, bad_val), which returns 
# a cleaned dictionary without any keys with the value bad_val

# The parameters of the function are the dictionary d 
# to be processed and the value bad_val to be disposed of together with its key.

# Example:

# clean_dict_value ({'a': 5, 'b': 6, 'c': 5}, 5) -> {'b': 6}, because 5 was a value for both a and c keys to get rid of.


# 3b Write clean_dict_values ​​(d, v_list), which returns a cleaned dictionary

# The parameters of the function are the dictionary d to be 
# processed and the list of values ​​v_list to get rid of.

# clean_dict_values ​​({'a': 5, 'b': 6, 'c': 5, 'd':3}, [3,4,5]) -> 
# {'b': 6} because 3 and 5 were in the list of values to delete.


# PS. Remember we can use del d['a'] only if the key 'a' exists.

# !! When resizing a dictionary, we are not allowed to iterate at the same time!


# There are two options: either walk through the copy 
# my_dict.copy.items(), or build a new dictionary. 
# Dictionary comprehension would be one option.

#3A 

def clean_dict_value_3a(d, bad_val):
    clean_dict = {k: v for k, v in d.items() if v != bad_val}
    return clean_dict

my_dict = {'m': 1, 'y': 2, 'e': 3}
print(my_dict)
print(clean_dict_value_3a(my_dict, 2))
print(my_dict)
new_dict = clean_dict_value_3a(my_dict, 2)
print(my_dict)
print(new_dict)

#{'m': 1, 'y': 2, 'e': 3}
#{'m': 1, 'e': 3}
#{'m': 1, 'y': 2, 'e': 3}
#{'m': 1, 'y': 2, 'e': 3}
#{'m': 1, 'e': 3}

# Ex. 3b
# OUT OF PLACE
def clean_dict_values_3b(d, bad_list):
    return {k: v for k, v in d.items() if v not in bad_list}


print(clean_dict_values_3b({'m': 1, 'y': 2, 'e': 3}, [1, 2]))

cleaned_dict = clean_dict_values_3b(my_dict, [1, 2])
print(my_dict)
print(cleaned_dict)

#{'e': 3}
#{'m': 1, 'y': 2, 'e': 3}
#{'e': 3}