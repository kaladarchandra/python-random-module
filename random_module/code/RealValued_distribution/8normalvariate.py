import matplotlib.pyplot as plt
import random

# normal distribution mean is 4 and standard deviation is 2.
# change the standard deviations for the same mean, it will be fun .
# It is good idea to expand the bins as the normal distribution is indefinite.
dist = [ random.normalvariate(4, 2) for i in range(10000)]           
bins = [-1 + (x/10) for x in range(200)]          
                                                                                                             
                                                                                

plt.hist(dist, bins)                                                                            

plt.show()


