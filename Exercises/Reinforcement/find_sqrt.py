num = float(input("Enter a number: "))
num_sqrt = num ** 0.5
print("The square root of %0.3f is %0.3f" %(num, num_sqrt))

"""
In the program above, we ask the user for a number and find the square root using the ** exponent
operator. The program works for all positive real numbers. But for negative or complex
numbers, it can be done as follows
"""
# Find square root of real or complex numbers
# import the complex math module
import cmath

num = eval(input("Enter a number: "))
num_sqrt = cmath.sqrt(num)
print("The square root of {0} is {1:0.3f}+{2:0.3f}j".format(num, num_sqrt.real, num_sqrt.imag))

"""
In this program we use the sqrt() function in the cmath(complex math) module. Notice that
we have the eval() function instead of float to convert complex numbers as well. Also
notice the way which the output is formatted.
"""
