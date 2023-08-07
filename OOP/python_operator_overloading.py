"""
Python operators work for built-in classes. But same operator behaves differently with different
types. For example, the + operator will, perform arithmetic addition on two numbers, merge two
lists and concatenate two strings. This feature in Python, that allows same operator to have
different meaning according to the context is called operator overloading.

So what happens when we use them with objects of a user-defined class? Let us consider the
following class, which tries to simulate a point in 2-D coordinate system.
"""
# class Point:
#     def __init__(self, x = 0, y = 0):
#         self.x = x
#         self.y = y

"""Now when we try to add two points that we create as follows."""
# p1 = Point(2, 3)
# p2 = Point(-1, 2)
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

# p1 = Point(2, 3)
# print(p1)

"""
That did not print well. But if we define __str__() method in our class, we can control how it gets printed.
"""
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

p1 = Point(2, 3)
print(p1) 

"""
That's better. Turns out that this same method is invoked when we use the built-in function
str() or format()
"""
print(str(p1))
print(format(p1))

"""
So when you do str(p1) or format(p1), Python is internally doing p1.__str__(). Hence the
name, special functions.
"""

# Overloading the + operator
"""
To overload + sign, we will need to implement __add__() function in the class. We will
return a Point object of the coordinate sum.
"""
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

# now lets try that addition again.
p1 = Point(2, 3)
p2 = Point(-1, 2)
print(p1 + p2)

"""
What actually happens is that, when you do p1 + p2, Python will call p1.__add__(p2) which in
turn is Point.__add__(p1,p2). Similarly, we can overload other operators as well.
"""