"""
The format() method that is available with the string oject is very versatile and powerful in
formating strings. Format strings contains curly braces {} as placeholders or replacement fields
which gets replaced. We can use positional arguments or keyword arguments to specify the
order.
"""

# default implicit order
print("{}, {} and {}".format("John", "Bill", "Sean"))

# order using positional arguments
print("{1}, {0} and {2}".format("John", "Bill", "Sean"))

# order using keyword arguments
print("{s}, {b} and {j}".format(j="John", b="Bill", s="Sean"))
