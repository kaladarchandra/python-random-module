# random.random()
# constructing a histogram 

import numpy as np
import matplotlib.pyplot as plt
import random

distribution = random.random()

x = [ random.betavariate(0.5, 0.5) for i in range(1000)]
x1 = [ random.betavariate(5, 1) for i in range(1000)]
x2 = [ random.betavariate(1, 3) for i in range(1000)]

bins = [ 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]



plt.hist(x, bins)
plt.hist(x1, bins)
plt.hist(x2, bins)

plt.show()
