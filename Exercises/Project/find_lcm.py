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