# Python if...elif...else and Nested if
# Python while loop

"""
An Armstrong number, also known as narcissistic number, is a number that is equal to the sum
of the cubes of its own digits. For example, 370 is Armstrong number since 370=3*3*3 + 
7*7*7 + 0*0*0
"""
# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

# display the results
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

"""
Here, we ask the user for a number and check if it is an Armstrong number. We need to calculate
the sum of the cube of each digit. So, we initialize the sum to 0 and obtain each digit number by 
using the modulus operator %. Remainder of a number when it is divide by 10 is the last digit of
that number. We take the cubes using exponent operator. Finaly, we compare the sum with the
original number and conclude that is Armstrong number if they are equal.
"""
