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

# Exceptions are objects that can be examined when caught. To do so, an identifier must
# be established with a syntax as follows
try:
    fp = open("sample.txt")
except Exception as e:
    print("Unable to open the file:", e)

# In this case, the name "e", denotes the instance of the exception that was thrown, and
# printing it causes a detailed error message to be displayed.

# A try statement may handle more than one type of exception. For example,
# consider the following code.
age = int(input("Enter your age in years:"))

# The above code could fail for a variety of reasons. The call to input will raise an EOFError
# if the console input fails. If the call to input completes successfully, the
# int constructor raises "ValueError" if the user has not entered characters representing
# a valid integer. If we want to handle two or more types of errors in the same way, we
# can use a single except-statement, as in the following code.
age = -1
while age <= 0:
    try:
        age = int(input("Enter your age in years: "))
        if age <= 0:
            print("Your age must be positive")
    except (ValueError, EOFError):
        print("Invalid response")

# we use the tuple, (ValueError, EOFError), to designate the types of errors that we
# wish to catch with the except-clause. In this case, we catch either error,
# print a response, and continue with another pass of the enclosing while loop.

# In order to provide different responses to different types of errors, we may use
# two or more except-clauses as part of a try-structure. We might wish to provide
# a more specific error message, or perhaps to allow the exception to interrupt the
# loop and be propagated to a higher context. We could implement such behaviour as follows:
age = - 1
while age <= 0:
    try:
        age = int(input("Enter your age in years: "))
        if age <= 0:
            print("Your age must be positive")
    except ValueError:
        print("That is an invalid age specification")
    except EOFError:
        print("There is an unexpected error reading input.")
        raise # let's re-raise this exception