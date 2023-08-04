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

# Keyword Arguments

"""
When we call a function with some values, these values get assigned to the arguments according
to their position. For example in the function call above, "Bruce" got assigned to name and "How do you do"
got assigned to msg.

Python allows functions to be called using keyword arguments. When we call functions in this
way, the order(position) of the arguments can be changed. Following calls to the above function
are all valid and produce the same result.
"""
greet(name="Bruce", msg="How do you do?")       # 2 keyword arguments
greet(msg="How do you do?", name="Bruce")       # 2 keyword arguments (out of order)
greet("Bruce", msg="How do you do?")            # 1 positional argument, 1 keyword argument

"""
As we can see, we can mix positional arguments with keyword arguments during a function call.
But we must keep in mind that keyword arguments must follow positional arguments. Having a
positional argument after keyword arguments will result into errors.
"""