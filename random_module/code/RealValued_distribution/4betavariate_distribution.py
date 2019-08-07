import matplotlib.pyplot as plt
import random


# output from beta distribution with alpha = 5 and beta = 1.
dist = [ random.betavariate(5, 1) for i in range(1000)]        
bins = [ 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]         # observe the bars.

plt.hist(dist, bins)

plt.show()


