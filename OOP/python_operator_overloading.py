"""
Python operators work for built-in classes. But same operator behaves differently with different
types. For example, the + operator will, perform arithmetic addition on two numbers, merge two
lists and concatenate two strings. This feature in Python, that allows same operator to have
different meaning according to the context is called operator overloading.

So what happens when we use them with objects of a user-defined class? Let us consider the
following class, which tries to simulate a point in 2-D coordinate system.
"""
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

"""Now when we try to add two points that we create as follows."""
p1 = Point(2, 3)
p2 = Point(-1, 2)
# print(p1 + p2)

"""
Whoa! That's a lot of complains. TypeError was raised since Python didn't know how to add
two Point objects together. However, the good news is that we can teach this to Python through
operator overloading. But first, let's get a notion about special functions.
"""

# Special Functions in Python
"""
These are class functions that begins double underscore(__). The __init__() function is one of them.
It gets called everytime we create a new object of that class. There are a ton of special
functions in Python

Using special functions, we can make our class compatible with built-in functions
"""

