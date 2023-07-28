# An exception is thrown by executing the "raise" statement,with an appropriate
# instance of an exception class as an argument that designates the problem.
# For example,if a function for computing a square root is sent a negative value as a parameter,
# it can raise an exception with the command

# raise ValueError("x", "cannot be negative")

# When checking the validity of parameters sent to a function, it is customary
# to first verify that a parameter is of an appropriate type, and then to verify
# that it has an appropriate value. For example, the sqrt function in Python's math
# library performs error-checking that might be implemented as follows:
def sqrt(x):
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric")
    elif x < 0:
        raise ValueError("x cannot be negative")
    # do the real work here

# Checking the type and value of each parameter demands additional execution time
# and if taken to an extreme seems counter to the nature of Python. Consider
# the built-in sum function which computes a sum of collection of numbers. An
# implementation with rigorouss error-checking might be written as follows:
def sum(values):
    if not isinstance(values, collections.Iterable):
        raise TypeError("parameter must be an iterable type")
    total = 0
    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError("elements must be numeric")
        total = total + v
    return total

# The abstract base class, "collections.Iterable" includes all of Python's iterable
# containers types that guarantee support for the for-loop syntax(e.g., list, tuple, set);
# Within the body of the for loop, each element is verified as numeric before being added to
# the total. A far more direct and clear implementation of this function
# can be written as follows:
def sum(values):
    total = 0
    for v in values:
        total = total + v
    return total


# Catching an Exception
