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