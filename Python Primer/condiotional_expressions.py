# Python supports a "conditional expression" syntax that can replace a simple control
# structure. The general systax is an expression of the form

# expr1 if condition else expr2

# This compound evaluates to expr1 if the condition is True, and otherwise evaluates
# to expr2

# As an example, consider the goal of sending the absolute value of a variable, n, to 
# a function(and without relying on the built-in abs function, for the sake of the example).
# Using a traditional control structure, we might accomplish this as follows:

# if n >= 0:
#     param = n
# else:
#     param = -n
# result = foo(param) # call the function

# with the conditional expression syntax, we can directly assign a value to variable, param as follows:

# param = n if n >=0 else -n # pick the appropriate value
# result = foo(param) # call the function

# In fact, there is no need to assign the compout expression to a variable. A conditional expression can 
# itself serve as a parameter to the function, written as follows


# result = foo(n if n >= 0 else -n)

# Sometimes the mere shortening of source code is advantageous because it avoids the distraction of a more cumbersome
# control structure. However, it is recommended that a conditional expression be used only when it imporoves
# the readability of the source code, and when the first of the two options is the more "natural" case, given
# its prominence in the syntax.