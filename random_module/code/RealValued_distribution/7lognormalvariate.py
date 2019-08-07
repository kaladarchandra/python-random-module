import matplotlib.pyplot as plt
import random

# Lognormal distribution
dist = [ random.lognormvariate(2, 0.7) for i in range(10000)]           
bins = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8]                     
                                                                                                        

plt.hist(dist, bins)                                                                            

plt.show()


