# Python if...elif...else and Nested if
# Python while loop

"""
A fibonacci sequence is the integer sequence of 0,1,1,2,3,5,8.... The first two terms are 0 and
1. All other terms are obtained by adding the preceding two terms. This means to say the nth
term is the sum of (n-1)th and (n-2th) term
"""

# take input from the user

nterms = int(input("How many terms? "))

# first two terms
n1 = 0
n2 = 1
count = 2

# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer!")
elif nterms == 1:
    print("Fibonacci sequence:")
    print(n1)
else:
    print("Fibonacci sequence:")
    print(n1, ",", n2, end=", ")
    while count < nterms:
        nth = n1 + n2
        print(nth, end=' , ')
        # update value
        n1 = n2
        n2 = nth
        count += 1

"""
Here, we ask the user for the number of terms in the sequence. We initialize the first term to 0
and the second term to 1. If the number of terms is more than 2, we use a while loop to find the
next term in the sequence by adding the preceding two terms. We the interchange the variables
(update it) and continue on with the process.
"""
