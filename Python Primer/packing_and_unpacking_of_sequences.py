# Python provides two additional conveniences involving the treatment of tuples and
# other sequence types. This first is rather costmetic. If a series of comma-separeted
# expressions are given in a larger context, they will be treated as a single tuple even
# if no enclosing parenthesis are provided. For example, the assignment
data = 2, 4, 6, 8
# results in identifier, data, being assigned to the tuple (2, 4, 6, 8). This behavior is called
# "automatic packing" of a tuple.
# one common use of packing is when returning multiple values from a function. If the body of a 
# function executes the command,

# return x, y

# it will be formally returning a single object that is a tuple (x, y).

# As a dual to packing behavior, Python can automatically "unpack" a sequence,
# allowing one to assign a series of individual identifiers to the elements
# of sequence. As an example we write

a, b, c, d = range(7, 11)

# which has the effect of assigning a=7, b=8, c=9 and d=10, as those are the four
# values in the sequence returned by the call range.
# For this syntax, the right-hand side expression can be any iterable type, as long
# as the number of variables on the left-hand side is the same as the number of elements
# in the iteration.

# This technique can be used to unpack tuples returned by a function. For example,
# the built-in function, divmod(a, b) returns the pair of values (a // b, a % b)
# associated with an integer division. Although the caller can consider the return
# to be a single tuple, it is possible to write

quotient, remainder = divmod(a, b)

# to separately identify the two entries of the returned tuple. This syntax can also be
# used in the context of a for loop, when iterating over a sequence of iterables, as in

for x, y in [(7, 2), (5, 8), (6, 4)]:
    pass

# In this example, there will be three iterations of the loop. During the first pass, x=7
# and y=3 and so on. This style of loop is quite commonly used to iterate through
# key-value pairs that are returned by the items() method of the dict class as in:

# for k, v in mapping.items():
