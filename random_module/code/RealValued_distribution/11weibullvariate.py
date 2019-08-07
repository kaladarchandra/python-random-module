import matplotlib.pyplot as plt
import random


# weibull distribution with scale = 0 and shape = 1.5
dist = [ random.weibullvariate(1, 1.5) for i in range(1000)]    
bins = [-10, 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]       
                                                                                                       
plt.hist(dist, bins)

plt.show()




