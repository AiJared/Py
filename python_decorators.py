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
"""
Functions and methods are called "callable" as they can be called. In fact, any object which
implements the special method __call__() is termed callable. So, in the most basic sense, a
decorator is a callable that returns a callable. Basically, a decorator takes in a function, adds
some functionality and returns it.
"""
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

ordinary()

"""Let's decorate this ordinary function"""
pretty = make_pretty(ordinary)
pretty()

"""
In the example shown above, make_pretty() is a decorator. In the assignmet step
pretty = make_pretty(ordinary)

The function ordinary() got declared and the returned function was given the name pretty.
We can see that the decorator function added some new functionality to the original function.
This is similar to packing a gift. The decorator acts a wrapper. The nature of the object that
got decorated(actual gift inside) does not alter. But now, it looks pretty(since it got decorated).

Generally, we decorate a function and reassign it as, 
"""
ordinary = make_pretty(ordinary)

"""
This is a common construct and for this reason, Python has a syntax to simplify this. We can use
the @ symbol along with the name of the decorator function and place it above the definition of
the function to be decorated. For example.
"""
@make_pretty
def ordinary():
    print("I am ordinary")

"""is equivalent to"""
def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)

"""This is just a syntactic sugar to implement decorators."""

# Decorating Functions with Parameters
"""
The above decorator was simple and it only worked with functions that did not have any
parameters. What if we had functions that took in parameters like below?
"""
def divide(a, b):
    return a / b

"""
This function has two parameters, a and b. We know, it will give error if we pass in b as 0.
"""

"""
Now let's make a decorator to check for this case that will cause the error.
"""
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a ,"and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return
        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    return a / b

"""This new implementation will return None if the error condition arises."""
a = divide(2, 5)
print(a)
print(divide(2,0))

"""
In this manner, we can decorate functions that take parameters. A keen observer will notice that
parameters of the nested inner() function inside the decorator is same as the parameters of
functions it decorates. Taking this into account, now we can make general decorators that work
with any number of parameter. In Python, this magic is done as function()
"""
