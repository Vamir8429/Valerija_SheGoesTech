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