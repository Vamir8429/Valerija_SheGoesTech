import matplotlib.pyplot as plt
#import numpy as np

# TODO
# 1. plot a graph of x and y
# x would be values from -10 to 10 (21 values)
# y would be the cube of x + 5

# you could use a different library than matplotlib but it is the most popular one
# will will explore other ones later on in the course

x = list(range(-10,11))
#print(x)
#[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [(n+5)**3 for n in x]
#print(y)
# [-125, -64, -27, -8, -1, 0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375]

#plot
fig, ax = plt.subplots()
ax.plot(x, y)

plt.title("My first plot")
plt.xlabel("My list of values")
plt.ylabel("My cubed values")

plt.show()
