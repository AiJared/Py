# Python if...elif...else and Nested if
"""
In this program, the user enters a number and it checks if the number is
positive, negative or zero.
"""
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

"""
Here, we have used tue if...elif...else statement. The same thing can be done using nested if
statement as follows.
"""

# This time use nested if to solve the problem
num = float(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")