"""
Set is an unordered collection of items. Every element is unique(no duplicates) and must be 
immutable. However, the set itsetf is mutable (we can add or remove items). Sets can be used to
perform mathematical set operations like union, intersection, symmetric difference etc.
"""

# Creating a Set in Python
"""
A set is created by placing all the items (elements) inside curly braces {}, separated by comma or
by using the built-in function set(). It can have any number of items and they may be of 
different types (integer, float, tuple, string etc.). But a set cannot have a mutable element, like
list, set or dictionary, as its element.
"""
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# set from a list
a = set([1, 2, 3])
print(a)

"""
Creating an empty set is a bit tricky. Empty curly braces {} will make an empy dictionary in
Python. To make a set without any elements we use the set() method without any argument.
"""
i = set()
print(type(a))