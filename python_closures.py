"""
A function defined inside another function is called a nested function. Nested functions can
access variables of the enclosing scope. In Python, these non-local variables are read only by
default and we must declare them explicitly as nono-local(using nonlocal keyword) in order to
modify them. Following is an example of a nested function accessing a non-local variable.
"""
def print_msg(msg):
    """This is the outer enclosing function."""

    def printer():
        """This is the inner nested function"""
        print(msg)
    
    printer()

"""We execute the function as follows."""
print_msg("Hello")

"""
We can see that the nested function printer() was able to access the non-local variable msg of
the enclosing function. In the example above, what would happen if the last line of the function
print_msg() returned the printer() function instead of calling it? This means the function was
defined as follows.
"""
def print_msg(msg):
    """This is the outer enclosing function"""

    def printer():
        """This is the inner nested function"""
        print(msg)

    return printer  # this got changed
"""Now let's try calling this function."""
another = print_msg("Hello")
another()

"""
The print_msg() function was called with the string "Hello" and the returned
function was bound to name "another". On calling another(), the message was still
remembered although we had already finished executing the print_msg() function. This 
technique by which some data("Hello") gets attached to the code us called closure in Python.

This value in the enclosing scope is remembered even when the variable goes out of scope or the
function itself is removed from the current namespace.
"""
# When Do We Have a Closure?
"""
As seen from the above example, we have a closure in Python when a nested function refrences
a value in its enclosing scope. The creteria that must be met to create a closure in Python are
summarized in the following points.

1. We must have a nested function (function inside a function)
2. The nested function must refer to a value defined in the enclosing function.
3. The enclosing function must return the nested function.
"""
