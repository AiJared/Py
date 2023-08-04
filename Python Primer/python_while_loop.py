"""The while loop in Python is used to iterate over a block of code as long as the test expression
(condtion) is True. We generally use this loop when we don't know beforehand, the number of
times to iterate.

In while loop, test expression is checked first. The body of the loop is entered only if the
test_expression evaluates to True. After one iteration, the test expression is checked again.
The process continues until the test_expression evaluates False.

In Python, the body of the while loop is determined through indentation. Body starts with
indentation and the first unindented line marks the end. Python interprets any non-zero value
as True. None and 0 are interpreted as False.
"""

# Example

# Program to add natural
# numbers upto n where
# n is provided by the user

# take input from the user
n = int(input("Enter n: "))

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i += 1          # update counter

# print the sum
print("The sum is", sum)