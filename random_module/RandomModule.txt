As of 3.7.3 this are the random modules methods.
This is the exact ordering as in the module itself. 
These methods are of different categories, such that some work with sequences, some with integers ...

If the entire module is in single text file it will be overwhelming to go through it so i have explained each category in separated text file.
And it will allow the learner to go through the module in step wise fashion, learning categories one by one.
I have explained Bookkeeping functions at last, cause we could understand it intuitively after understanding all categories.




module name : random

Bookkeeping functions
-----------------------------------------------------------------------------
1)random.seed(a=None, version=2)
2)random.getstate()
3)random.setstate(state)
4)random.getrandbits(k)



Functions for integers
------------------------------------------------------------------------------
1)random.randrange(stop)
  random.randrange(start, stop[, step])
2)random.randint(a, b)



Functions for sequences
------------------------------------------------------------------------------
1)random.choice(seq)
2)random.choices(population, weights=None, *, cum_weights=None, k=1)
3)random.shuffle(x[, random])
4)random.sample(population, k)



Real-valued distributions
------------------------------------------------------------------------------
1)random.random()
2)random.uniform(a, b)
3)random.triangular(low, high, mode)
4)random.betavariate(alpha, beta)
5)random.expovariate(lambd)
6)random.gammavariate(alpha, beta)
7)random.gauss(mu, sigma)
8)random.lognormvariate(mu, sigma)
9)random.normalvariate(mu, sigma)
10)random.vonmisesvariate(mu, kappa)
11)random.paretovariate(alpha)
12)random.weibullvariate(alpha, beta)



