# 1. An "iterator" is an object that manages an iteration through a series of values. If
# variable, i, identifies an iterator object, then each call to the built-in function,
# next(i), produces a subsequent element from the underlying series, with a
# StopIteration exception raised to indicate that there are no further elements.

# 2. An "iterable" is an object, obj, that produces an iterator via the syntax iter (obj)
# By these definitions, an instance of a list is an iterable but not itself an iterator.

data = [1, 2, 4, 8]
# it is not legal to call next(data). However, an iterator
# object can be produced with syntax 
i = iter(data) 
# and then each subsequent call to next(i) will return an element of that list.
next(i)
# The for-loop syntaxt in python simply automates this process, creating an iterator for the
# given iterable, and then repeatedly calling for the next element until catching the 
# StopIteration exception

# Generators

# The most convenient technique for creating iterators in Python
# is through the use of "generators". A generator is implemented 
# with a syntax that is very similar to a function, but instead
# of returning values, a "yield" statement is executed to indicate
# each element of the series. As an example, consider the goal of
# determining all factors of a positive integer.
# For example, the number 100 has factors 1, 2, 3, 4, 5, 10, 20, 25, 50, 100.
# A traditional function might produce and return a list containing all factor
# implemented as:
def factors(n): # traditional function that computes factors
    results = [] # store factors in a new list
    for k in range(1, n+1): 
        if n % k == 0:  # divides evenly, thus k is a factor
            results.append(k) # add k to the list of factors
    return results # return the entire list

# in contrast, an implemetation of a "generator" for computing those factors
# could be implemented as follows:
def factors(n): # generator that computes factors
    for k in range(1, n+1):
        if n % k == 0: # divides evenly, thus k is a factor
            yield k # yield this factor as next result

# notice use of the keyword "yield" rather than "return" to indicate a result.
# This indicates to Python that we are defining a generator, rather than a
# traditional function. It is illegal to combine yield and return statements 
# in the same implementation.

# We can greatly improve the efficiency of our generator for computing factors of a number
# n, by only testing values up to the square root of that number, while reporting the factor
# n // k that is associated with each k (unless n // k). We might implement
# such a generator as follows:
def factors(n): # generator that computes factors
    k =1
    while k + k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n: # special case if n is perfect square
        yield k

# We should not that this generator differs from our first version
# in that the factors are not generated in strictly increasing order.
# For example, factors(100) generates the series
# 1, 100, 2, 50, 4, 25, 5, 20, 10

# A generator can effectively produce an infinite series of values. As
# an example, the Fibonacci numbers form a classic mathematical sequence,
# starting with value 0, then value 1, and each subsequent value being the 
# sum of the preceeding values. Hence, the Fibonacci series begins as: 0, 1, 1, 2, 3, 5, 8, 12 ...
def fibonacci():
    a = 0
    b = 1
    while True: # keep going...
        yield a # report value a, during this pass
        future = a + b
        a = b # this will be next value reported
        b = future  # and subsequently this
        