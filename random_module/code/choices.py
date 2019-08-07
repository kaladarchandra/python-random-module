# we are plotting pie graph
# This is about choices method that takes optional weights parameter.
# And it gives random numbers from the distribution according to the weight of the each item.
# It will be good if you know pie chart creation else just see the ouput according to the ratio

import matplotlib.pyplot as plt
import random

# Just printing the pie chart , don't worry if you don't understand the code.
# But you should know how the pie chart works. Total circle is all the frequencies.
# And the parts are frequency of each category.
def pie(fqs,popu, weits):
    plt.pie(fqs, labels = popu, startangle = 90)
    title = 'population = {0}\n weights = {1}'.format(popu, weits)
    plt.title(title)
    
    plt.show()


# To find the frequency of x items, in y.
# x is the input list and y is the large list of choices output.
def rfreq(x, y):
    fx = []

    for i in x :
        fx.append( y.count(i) )   # We are appending the frequency of each element of x
                                                    # y.count(i) returns how many times the element named i is in y.
                                                    # Thus we find the frequency of every element of x .
    return fx



population = [1, 2, 3, 4]                                 # The list we give to choices
weights = [25,25,25,25]                                # Weights of the population, 1 should be in it 50% and 2 and 3 are 25% and 25%.

choices = random.choices(population, weights, k = 1000)         # 1000 random choices from the list population.
flist = rfreq(population, choices)          # List containing the frequency of each item in the population in choices.


pie(flist, population, weights) # printing the pie chart

print(choices)

# change the population and weights , execute.
# see how the different weights corresponds to different frequency in the result.
# make sure weight add up to hundred.



