This is just a normal visulization of the distributions.
You need to know how to plot a histogram to understand the code here.
But even if you don't it's okay the code is explained along the way.

Good visulizers might write their own code to have better visulizations.

HISTOGRAM.
----------------------------------------------------------------------------------------------------
Histogram is similar to a bar chart except bars are continuous. 
That is there are bunch of real numbers from 1 to 5 with duplicates.
numbers = [1, 1.2, 3.6, 5.01, 4.3, 2.2, 2, 2]
There are 2 numbers from 1 upto not including 2(1, 1.2) and  2 is the frequency of bar 1-2.
Similarly 3 is height of 2-3, 1 is height of bar 3-4, 1 is height of bar 4-5.


copy paste the code in script file and execute.
-----------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt

numbers = [1, 1.2, 3.6, 5.01, 4.3, 2.2, 2, 2]
bins = [1, 2, 3, 4, 5] 								# This is the input we give to the hist method, observe carefully, these make up the x axis bars. 
													# In this manner 1-2, 2-3, 3-4, 4-5. Number of x that are 1<= x < 2 will be the height of the bar 1-2.

plt.hist(numbers, hist)								# plots the histogram
plt.show()											# displays



Now check the code of distributions. Change the parameters of distributions and bins according to them and execute.
This way you could explore the distribution.



