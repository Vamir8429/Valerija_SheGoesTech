# 2. Dictionary editor



# Write replace_dict_value(d, bad_val, good_val), 
# which returns a dictionary with changed values

# The parameters of the function are the dictionary d 
# to be processed and the values ​​bad_val to be changed to good_val

# clean_dict_value ({'a': 5, 'b': 6, 'c': 5}, 5, 10) -> 
# {'a': 10, 'b': 6, 'c': 10}, because 5 was the value to be replaced

dictionary = {
    'a': 5,
    'b': 6,
    'c': 5}
def replace_dict_value(d, bad_val, good_val):
    clean_dict = {}
    for key in d:
        if d[key] == bad_val:
            clean_dict[key] = good_val
        else:
            clean_dict[key] = d[key]
    print (clean_dict)
 
replace_dict_value(dictionary, 5, 10)

#{'a': 10, 'b': 6, 'c': 10}