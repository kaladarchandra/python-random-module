# we are constructing histogram.
import matplotlib.pyplot as plt
import random



dist = [ random.random() for i in range(1000)]                     #  Produces 1000 ouputs, this is the distribution.
bins = [ 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]         #  bars are 0.0-0.1 and 0.1-0.2   and  0.2-0.3 ... upto 0.9 - 1.0.
                                                                                                         #  If you dont understand type histogram in google and then read readme.txt.

plt.hist(dist, bins)

plt.show()

# press F5 . observe outputs are evenly distributed from 0 to 1.
