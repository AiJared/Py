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

"""
The format method can have optional format specifications. They are separated from field
name using colon. For example, we can left-justify <, right-justify >, or center ^ a string in the
given space. We can also format integers as binary, hexadecimal etc. and floats can be rounded
or displayed in the exponent format.
"""

# formating integers
print("Binary representation of {0} is {0:b}".format(12))

# formatting floats
print("Exponent representation: {0:e}".format(1566.345))

# round off
print("One third is {0:.3f}".format(1/3))

# string alignment
print("|{:<10}| {:^10}| {:>10}".format("butter", "bread", "ham"))
