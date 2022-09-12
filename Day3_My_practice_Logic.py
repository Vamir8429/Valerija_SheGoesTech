# # # # Boolean Algebra kas ir pamatā visiem datoriem (un elektronikai)
is_sunny = True
print(is_sunny) #True
print("let the toggling begin with not")
is_sunny = not is_sunny # Toggle pattern we reverse the logic
#Toggle - is like a switch 
print(is_sunny) #False
is_sunny = not is_sunny # we reverse the logic
print(is_sunny) #True
is_sunny = not is_sunny # we reverse the logic
print(is_sunny) #False
is_overcast = not is_sunny #  but if it is not sunny then it is overcast
print(is_overcast, is_sunny) #True, False 

print(not True, not False) # negation Python uses not, some other language use ! #False, True 

# # # # logical conjunction and in Python we use and (not &&)
print("Testing and logic, logical conjuction")
print(True and True) # only True here
print(True and False)  # only False here
print(False and True) # only False here
print(False and False) # last 3 are False
# # #

# # # we can have conjuctions on multiple statements
print(is_sunny)
print(2*2 == 4 and is_sunny and 5 > 1) #False
## lazy evaluation in the above first false and rest is not evaluated
# # # # above is False since in a chain one False statement will ruin everything

a = 0
#print(551/a)    # will throw an error
print( a != 0 and 10 / a) # so 10 / a will not run, so no error will be thrown #False
#
is_sunny = not is_sunny # we reverse the logic #False
print(2*2 == 4 and is_sunny and 5 > 1 and 5*5 > 10) #True

# # # logical disjunction with or (Python uses actual or not ||)
print(True or True) #True
print(True or False) #True
print(False or True) # all 3 of the above ar True
print(False or False) # only one which is False
#

#
print("new")
are_pigs_flying = False
is_devil_skating = False
is_winter = True
print(are_pigs_flying or is_devil_skating or is_winter or 2 * 2 == 5) 
# so True...we just need one True statement
is_a_good_day = are_pigs_flying or is_devil_skating or is_winter or 2 * 2 == 5 
print(is_a_good_day) #True
is_winter = False
print(are_pigs_flying or is_devil_skating or is_winter or 2 * 2 == 5)  
# when everything is False then whole statement is False
#

# # # XOR - True when only one side is True but False when both or none
is_raining = True
my_xor = (is_sunny and not is_raining) or (not is_sunny and is_raining) #False
print(False or False or True or False) # still True
# #