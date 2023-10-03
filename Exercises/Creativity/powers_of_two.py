# Python for loop
# Python Anonymous/Lambda Function

# Python program to display the powers of 2 using lambda function

# take number of terms from user
terms = int(input("How many terms? "))

# Use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))

# display the result
for i in range(terms):
    print("2 raised to power", i, "is", result[i])

"""
In this program, we have used anonymous(lambda) function inside the map() built-in function
to find the powers of 2
"""