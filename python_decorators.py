"""
Python has an interesting feature called "decorators" to add functionality to an existing code. This
is also called "metaprogramming" as a part of the program tries to modify another part of the
program at compile time.
"""

# Preliminaries

"""
We must be comfortable with the fact that, everything in Python(Yes! Even classes), are objects.
Names that we define are simply identifiers bound to these objects. Functions are no exceptions,
they are objects too(with attributes). Various different names can be bound to the same function
object. Here is an example.
"""
def first(msg):
    print(msg)

first("Hello")
second = first
second("Hello")

"""
Here,the names first and second refer to the same function object.

Now things start getting weirder. Functions can be passes as arguments to another function. If
you have used functions like map, filter and reduce in Python, then you already know about
this. Such function that take other functions as arguments are also called "higher order
functions". Here is an example of such a function
"""
def inc(x):
    """Function to increase value by 1"""
    return x + 1
def dec(x):
    """Function to decrease value by 1"""
    return x - 1

def operate(func, x):
    """A higher order function to increase or decrease"""
    result = func(x)
    return result

"""We invoke the function as follows."""
print(operate(inc, 3))
print(operate(dec, 3))

"""Furthermore, a function can return another function"""
def is_called():
    def is_returned():
        print("Hello")
    return is_returned

new = is_called()
new()

"""
Here, is_returned() is a nested function which is defined and returned, each time we call
is_called().

Finally, we must know about closures in Python.
"""

# Back to Decorators
