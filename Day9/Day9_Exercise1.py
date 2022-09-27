# 1. Min, Avg, Max

# Write a function get_min_avg_max (sequence) that returns a tuple 
# with three values, the smallest, the arithmetic mean, 
# and the largest value in the string, respectively.

# Example:

# get_min_avg_max ([0,10,1,9]) -> (0,5,10)

# the incoming sequence can be a tuple or a list with numeric values.

def get_min_avg_max(sequence):
    for item in sequence:
        max_value = max(sequence)
        min_value = min(sequence)
        mean_value = int(sum(sequence)/len(sequence))
        my_tuple = (min_value, mean_value, max_value)
        return my_tuple

print(get_min_avg_max([0,10,1,9])) #OUTPUT: (0, 5, 10)
print(get_min_avg_max([2,4,6.8])) #OUTPUT: (2, 4, 6.8)
#print(get_min_avg_max("vamir")) - Does not work with strings, how to fix?

