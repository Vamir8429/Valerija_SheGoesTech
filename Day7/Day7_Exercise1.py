#1. The Big Result

# Write an add_mult function that requires three parameters / arguments

# Returns the result that is the sum of the 2 smallest arguments multiplied by the largest argument value.

# PS Assume that numeric parameters will always be passed to the function, no need to check types

# Various solutions are possible (you are allowed to use other data structures inside function such as list).

# Example add_mult (2,5,4) -> will return (2 + 4) * 5 = 30

# PSS function should return the result, not print it.

#def add_mult(a,b,c):
#    a,b,c = sorted([a,b,c])
#    result = (f"Equation: ({a} + {b}) * {c}")
#    return result

def add_mult(a,b,c):
    my_list = [a,b,c]
    my_list.sort()
    print(f"({my_list[0]}+ {my_list[1]}) * {my_list[2]}")
    return (my_list[0] + my_list[1]) * my_list[2]

result = add_mult(2,4,3)
print(f"Result is {result}")