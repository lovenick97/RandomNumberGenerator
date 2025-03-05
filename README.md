# RandomNumberGenerator
Class to generate a number from a discrete probability distribution function.

## Breif:

Implement the method nextNum() and a minimal but effective set of unit tests. Implement in the language of your choice, Python is preferred,
but Java and other languages are completely fine. Make sure your code is exemplary, as if it was going to be shipped as part of a production
system.
As a quick check, given Random Numbers are [-1, 0, 1, 2, 3] and Probabilities are [0.01, 0.3, 0.58, 0.1, 0.01] if we call nextNum() 100 times
we may get the following results. As the results are random, these particular results are unlikely.
-1: 1 times
0: 22 times
1: 57 times
2: 20 times
3: 0 times

Do not use additional built ins or packages (beyond random and those needed for unit testing).

```import random
class RandomGen(object):
# Values that may be returned by next_num()
_random_nums = []
# Probability of the occurence of random_nums
_probabilities = []
def next_num(self):
"""
Returns one of the randomNums. When this method is called multiple
times over a long period, it should return the numbers roughly with
the initialized probabilities.
""" pass```

## Improvements

From the starting code above, adding an initialisation function opens the class up to taking new inputs. The class attributes _random_nums and _probabilities have been left in as hidden example inputs. Initialisataion includes basic checks to ensure permissible inputs, improvements could be achieved here using something like Pydantic which checks and validates inputs (less verbose).

Using external packages such as Numpy would significantly simplify the number generator method as the whole function could be implemented in one step using:

```np.random.choice(random_nums, p=probabilities)```

Moreover, the error coverage is very good and computational processes more effiecient.

## Questions/Thoughts
Writing unit tests for a stocastic function presents interesting challenges for stocastic models. How does one test for randomness effectively? I considered that for a single output we may want to confirm that a result was within some region within the expected output, a 99% confidence interval for instance. However, while the probability *p* of this test failing is 1%, the probability of at least 1 test failing across *t* unit tests increases ~ like *pt*. In a large project with many tests this could be trigger several false test failures. To work around this issue one can require a very low p (more stds from the mean), although this lowers confidence in the test. To Increase confidence one could use a very large n as relative variability increases with sqrt(n) meaning the confidence intervals become much tighter around expected values. However, a large n inreases time, compute, resource etc...

In practise, how are stocastic processes tested?


