# while loop
# functions
# function arguments
# user-defined functions

"""
The least common multiple (LCM) of two numbers is the smallest positive integer that is
perfectly divible by the two given numbers. For example, the LCM of 12 and 14 is 84.
"""

# define a function

def lcm(x, y):
    """This function takes two
    integers and returns the LCM."""

    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

# take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The LCM of", num1, "and", num2, "is", lcm(num1, num2))

"""
This program asks for two integers and passes them to a function which returns the L.C.M. In the
function, we first determine the greater of the two number since the LCM can only be greater
than or equal to the largest number. We then use an infinite while loop to go through that number
and beyond. In each iteration, we check if both input numbers perfectly divides our number.
If so, we store the number as LCM and break from the loop. Otherwise, the number is incremented
by 1 and the loop continues.
"""

"""
The above program is slower to run. we can make it more efficient by using the fact thay the
product of two numbers is equal to the product of least common multiple and greatest common
divisor of those two numbers.

Number1 * Number2 = LCM * GCD.

Here is a Python program to implement this.
"""

# define gdc function
def gcd(x, y):
    """
    This function implements euclidean algorithm
    to find the GCD
    """
    while (y):
        x, y = y, x % y
    return x

# define lcm function
def lcm(x, y):
    """This function takes two 
    integers and returns the LCM."""
    lcm = (x*y) // gcd(x, y)
    return lcm

# take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The LCM of", num1, "and", num2, "is", lcm(num1, num2))

"""
The output of this program is same as before. We have two functions gcd() and lcm(). We
require GCD of the numbers to calculate its LCM. So, lcm() calls the function gcd() to
accomplish this. GCD of two numbers can be calculated efficiently using the Euclidean
algorithm.
"""