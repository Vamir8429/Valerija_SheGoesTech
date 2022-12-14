import matplotlib.pyplot as plt
import random
x = [random.randint(0, 10) for _ in range(10000)]
# plot histogram of data
fig, ax = plt.subplots()
# # ideally this 11 should be calculated from the data but for now we'll just hard code it
ax.hist(x, bins=11, color='blue', edgecolor='black')
fig.suptitle('Histogram of Random Data')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
plt.show() # activates the plot in interactive mode