# Python operators
# Python if...elif...else and Nested if
"""
A number is even if division by 2 give a remainder of 0.
If remainder is 1, it is odd number.
"""
num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))