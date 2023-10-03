# Python if...elif...else and Nested if
# Python while loop

# Python program to find the sum of natural numbers upto n where n is
# provided by user

# take input from the user

num = int(input("Enter a number: "))

if num < 0:
    print("Enter a positive number")
else:
    sum = 0
    # use while loop to iterate untill zero
    while (num > 0):
        sum += num
        num -= 1
    print("The sum is", sum)

"""
Here, we ask the user for a number and display the sum of natural numbers upto that number.
We use while loop to iterate until the number becomes zero.

We could have solved the above problem without using any loops. From mathematics, we know 
that sum of natural numbers is given by n*(n+1)/2. We could have ussed this formula directly.
For example, if n=16, the sum would be (16*17)/2 = 136
"""

# The following function uses the mathematical formula to do the same
def sum_of_n_numbers():
    n = int(input("Enter the number of terms: "))
    sum = n*(n+1) / 2
    print("The sum is", sum)

sum_of_n_numbers()