# Python if...elif...else and Nested if
# Python while loop

"""
A program to ask a user for a range and display all Armstrong numbers in
that interval
"""

# take input from the user
lower = int(input("Enter lower value: "))
upper = int(input("Enter upper value: "))

for num in range(lower, upper):
    # initialize sum
    sum = 0

    # find the sum of the cube of each digit
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    
    if num == sum:
        print(num)
    
"""
Here, we ask the user for the interval in which we want to search for Armstrong numbers. We
scan through the interval and display all the numbers that meet the condition.
"""
