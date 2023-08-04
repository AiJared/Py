"""
In Python, anonymous function is a function that is defined without a name. While normal
functions are defined using the def keyword, in Python anonymous functions are defined using
the lambda keyword. Hence, anonymous functions are also called lambda functions.
"""

# Lambda Functions

"""
Lambda functions can have any number of arguments but only one expression. The expression is
evaluated and returned. Lambda functions can be used wherever function objects are required.

Here is an example of a lambda function.
"""
double = lambda x: x * 2
print(double(5))

"""
In the above program, lambda x: x*2 is the lambda function. Here, x is the argument and x*2 
is the expression that gets evaluated and returned. This function has no name. It returns a
function object which is assigned to the identifier double. We can now call it as a normal
function as follow
"""

def double(x):
    return x * 2

"""
We use lambda function when we require a nameless function for a short period of time. In
Python, we generally use it as an argument to a higher-order function(a function that takes in
other functions as arguments). Lambda functions are used along with built-in functions like
filter(), map() e.t.c
"""

# Example use with filter()

"""
The filter function in Python takes in a function and a list of arguments. The function is 
called with all the items in the list and a new list is returned which contains items for which the
function evaluates to True.
"""

# Program to filter out only the even items from a list using filter() and lambda function
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0), my_list))
print(new_list)

# Example use with the map()

"""
The map() method in Python takes in a function and a list. The function is called with all the 
items in the list and a new list is returned which contains items returned by that function for each
item.
"""

# program to double each item in a list using map() and lambda function.
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x*2, my_list))
print(new_list)