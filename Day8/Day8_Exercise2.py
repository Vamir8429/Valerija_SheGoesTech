# 2. Dictionary editor



# Write replace_dict_value(d, bad_val, good_val), 
# which returns a dictionary with changed values

# The parameters of the function are the dictionary d 
# to be processed and the values ​​bad_val to be changed to good_val

# clean_dict_value ({'a': 5, 'b': 6, 'c': 5}, 5, 10) -> 
# {'a': 10, 'b': 6, 'c': 10}, because 5 was the value to be replaced

def replace_dict_value(d, bad_val, good_val):
    print(d)
    for key, value in d.items():
        if value == bad_val:
            d[key] = good_val
    print(d)
    return d

my_dict = {'a': 5, 'b': 6, 'c': 5}
print(my_dict)

new_dict = replace_dict_value(my_dict, 5, 12)
print(new_dict)
print(my_dict)