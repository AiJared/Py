# solve the quadratic equation ax**2 + bx + c = 0
# Coefficients a, b and c are provided by the user

# import cmath math module
import cmath

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("The solutions are {0} and {1}".format(sol1, sol2))
"""
In this program we ask the user for the coefficients of the quadratic equation. We have imported
the cmath module to perform complex square root. First we calculate the discriminant and then 
find the two solutions of the quadratic equation 
"""
