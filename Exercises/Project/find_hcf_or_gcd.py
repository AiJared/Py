# while loop
# for loop
# functions
# function arguments
# user-defined functions

""""
The highest common factor(HCF) or greatest common divisor (GCD) of two numbers is the
largest positive integer that perfectly divides the two given numbers. For example, the H.C.F of
12 and 14 is 2
"""

# define a function
def hcf(x, y):
    """This function takes two
    integers and returns the H.C.F"""

    # choose the smallest number
    if x > y:
        smaller = y
    else:
        smaller = x
    
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

# take input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The H.C.F of", num1, "and", num2, "is", hcf(num1, num2))

"""
The program asks for two integers and passes them to a function which returns the H.C.F. In the
function, we first determine the smaller of the two numbers since the HCF can only be less than
or equal to the smallest number. We the use the for loop to go from 1 to that number. In each
iteration we check if our number perfectly divides both the input numbers. If so, we store the
number as HCF. At the completion of the loop we end up with the largest number that perfectly
divides both the numbers.

The above method is easy to understand implement but not efficient. A much more efficient
method to find the HCF is the Euclidean algorithm.
"""
