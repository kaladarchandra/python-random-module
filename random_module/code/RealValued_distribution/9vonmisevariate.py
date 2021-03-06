import matplotlib.pyplot as plt
import random

# vonmises distribution angle is 4 radians and kappa is 1.
dist = [ random.vonmisesvariate(4, 1) for i in range(10000)]           
bins = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8]          
                                                                                                             
                                                                                                        

plt.hist(dist, bins)                                                                            

plt.show()


