# The combination of automatic packing and unpacking forms a technique known as 
# "simultaneous assignment", whereby we explicitly assign a series of values to a
# series of identifiers, using a syntax.

x, y, z = 6, 2, 5

# In effect, the right-hand side of this assignment is automatically packed into a tuple
# and then automatically unpacked with its elements assigned to the three identifiers
# on the left-hand side

# when using a simultaneous assignment, all of the expressions are evaluated
# on the right-hand side before any of the assignment are made to the left-hand side
# variables. This is significant, as it provides a convenient means for swapping the values
# associated with two variables

j, k = 2, 3
j, k = k, j

# with this command, j will be assigned to the old value of k and k will be assigned to the
# old value of j. Withoud simultaneous assignment, a swap typically requires more delicate use 
# of a temporary variable, such as

temp = j
j = k
t = temp

# With the simultaneous assignment, the unnamed tuple representing the packed
# values on the right-hand side implicitly serves as the temporary variable when
# performing such a swap

# The use of simultaneous assignments can greatly simplify the presentation of code.
# as an example, we reconsider the generator that produces the
# Fibonacci series. The original code requres separate initialization of variables a
# and b, respectively, to the values of b and a+b. At that time, we accomplished this
# with brief use of a third variable. With simultaneous assignments, that generator
# can be implemented more directly as follows:
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b