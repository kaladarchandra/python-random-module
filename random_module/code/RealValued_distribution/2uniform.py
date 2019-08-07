import matplotlib.pyplot as plt
import random


# output from uniform distribution with range 1 to 3.
# change the range to get the intuitive idea of the distribution. For example random.uniform(7, 17), change the bins accordingly.
dist = [ random.uniform(1, 3) for i in range(1000)]             
bins = [1, 1.5, 2, 2.5, 3]                                                                # We will group the outputs.Number of outputs that are between 1 and 1.5 are in one box,
                                                                                                         # number of outputs between 1.5 and 2 are in next box and so on.
                                                                                                        

plt.hist(dist, bins)                                                                        # x axis tells the category(bins) and height of the bin tells number of outputs in that category.

plt.show()


