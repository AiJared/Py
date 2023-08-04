# variable Function Arguments

"""
Up until now functions had fixed number of arguments. In Python there are other ways to define
a function which can take variable number of arguments. Three different forms of this type are
described below.
"""

# Default Arguments

"""
Function arguments can have default values in Python. We can provide a default value to an
argument by using the assignment operator(=). Here is an example
"""
def greet(name, msg="Good morning!"):
    """This function greets to
    the person with the provided message.
    If message is not provided, it defaults
    to "Good morning!" """
    print("Hello", name+ ", " + msg)

"""
In the above function, the parameter name does not have a default value and is required(mandatory)
during a call. On the other hand, the parameter msg has a default value of "Good morning!". So,
it is optional during a call. If a value is provided, it will overwrite the default value. Here are
some valid calls to this function.
"""
greet("Kate")
greet("Bruce", "How do you do?")

"""
Any number of arguments in a function can have a default value. But once we have a default
argument, all the other arguments to its right must also have default values. This means to say, non-
default arguments cannot follow default arguments.
"""

