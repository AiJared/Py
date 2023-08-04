"""
Recursion is the process of defining something in terms of itself. A physical example
would be to place two parallel mirrors facing each other. Any object in between them would be
reflected recursively.
"""

# Python Recursive Function

"""
We know that in Python, a function can call other functions. It is even possible for the function
to call itself. These types of construct are termed as recursive functions.

Following is an example of a recursive function to find the factorial of an integer. Factorial of a
number is the product of all the integers from 2 to that number.
"""

# find the factorial of a number
def recur_fact(x):
    """This is a recursive function
    to find the factorial of an integer."""

    if x == 1:
        return 1
    else:
        return (x * recur_fact(x - 1))
    
num = int(input("Enter a number: "))
if num >= 1:
    print("The factorial of", num, "is", recur_fact(num))

"""
In the above example, recur_fact() is a recursive function as it calls itself. When we call this
function with a positive integer, it will recursively call itself by decreasing the number. Each
function call multiples the number with the factorial of number-1 until the number is equal to
one.

Our recursion ends when the number reduces to 1. This is called the base condition. Every
recursive function must have a base condition that stops the recursion or else the function call
itself infinitely. We must avoid infinite recursions.
"""
