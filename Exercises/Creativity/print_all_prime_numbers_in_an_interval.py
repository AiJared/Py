# Python if...elif...else and Nested if
# Python for loop
# Python break and continue Statement

"""
In this program, we ask user for a range and display all
the prime numbers in that interval
"""
# take input from the user
lower = int(input("Enter a lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):
    # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)