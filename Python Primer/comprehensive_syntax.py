# A very common programming task is to produce one series of values based upon
# the processing of another series. Often, this task can be accompished quite simply
# in Python using what is know as "comprehensive syntax". We begin by demonstrating 
# the "list comprehension" as this was the first form to be supported by Python.

# As a concrete example, a list of the squares of the numbers from 1 to n, that is 
# [1, 4, 9, 16, 25,...n*n], can be created by traditional means as follows:
squares = []
n = 10
for k in range(1, n+1):
    squares.append(k*k)

# With list comprehension, this logic is expressed as follows:
squares = [k*k for k in range(1, n+1)]

# Python supports similar comprehension syntaxes that respectively
# produce a set, generator or dictionary. We compare those syntaxes using
# our example for producing the squares of numbers

[k*k for k in range(1, n+1)] # list comprehension
{k*k for k in range(1, n+1)} # set comprehension
(k*k for k in range(1, n+1)) # generator comprehension
{k:k*k for k in range(1, n+1)} # dictionary comprehension

# The generator syntax is particularly attractive when the results do not need
# to be stores in memory. For example, to compute the sum of the first n squares,
# the generator syntax, 
total = sum(k*k for k in range(1, n+1)) # is preferred to the use of an
# explicitly instantiated list comprehension as the parameter.
