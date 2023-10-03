"""
This algorithm is based on the fact that H.C.F of two numbers divides their difference as well. In
this algorithm, we divide the greater by smaller and take the remainder. Now, divide the smaller
by this remainder. Repeat until the remainder is 0.

For example, if we want to find the HCF of 54 and 24, we divide 54 by 24. The remainder is 6.
Now we divide 24 by 6 and the remainder is 0. Hence, 6 is the required HCF. We can do this in 
Python as follows:
"""

def hcf(x, y):
    """This function implements the Euclidian algorithm
    to find HCF of two numbers"""

    while(y):
        x, y = y, x % y
    return x

print(hcf(54, 24))

"""
Here, we loop until y becomes zero. The statement x, y = y, x % y does swapping of values is
Python. In each iteration weplace the value of y in x and the remainder (x % y) in y simultaneously.
When y becomes zero, we have HCF in x.
"""