import matplotlib.pyplot as plt
import random


# output from triangular distribution with maximum, minimum and mode 2, 8 and 5.
# change the range  and mode to get the intuitive idea of the distribution. For example random.triangular(2,5, 3), change the bins accordingly.
dist = [ random.triangular(2, 8, 4) for i in range(1000)]           
bins = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8]


plt.hist(dist, bins)                                                                            

plt.show()


