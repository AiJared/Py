# Python if...elif...else
# Python for loop

"""
The factorial of a number is the product of all the integers from 1 to that number.
It is not defined for negative numbers and the factorial of zero is, 0!=1.
"""
# take input from the user
num = int(input("Enter a number: "))
factorial = 1

# check if the number is negative, positive or zero
if num < 0:
    print("Sorry, factorial does not exist for negative numbers!")
elif num == 0:
    print("The factorial of", num, "is", 1)
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)
"""
Here, we take input from the user and check if the number is negative, zero or positive using
if...elif...else statement. If the number is positive, we use for loop and range() function
to calculate the factorial.
"""
