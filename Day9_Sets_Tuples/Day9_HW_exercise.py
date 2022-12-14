# write a function of 3 arguments all strings
# function should return lexigraphically ordered string of unique characters
# these unique characters must be present in BOTH  of the first two strings 
# BUT not in the third "badstring"

# example:
# "abcf", "fab", "boo"  returns -> "af" 
# because "a" is in both "abc" and "fab" but not in "boo"
# same goes for "f" it is present in both "good strings" but not in "badstring"
# notice "b" is not in the result because it is in the badstring.

# slightly harder way would be to use loops and if statements to check each character
# the easy way is to use sets and set operations 😊

# either approach is acceptable

def my_funct_strings(a, b, badstring):
    set1 = set(a)
    set2 = set(b)
    set3 = set(badstring)
    new_set1 = set1 - set3
    new_set2 = set2 - set3
    #return new_set1.intersection(new_set2)
    result = new_set1.intersection(new_set2)
    result = "".join(sorted(result))
    return result

print(my_funct_strings("abcf", "fab", "boo"))


