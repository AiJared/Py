# if...elif...else and Nested if
# while loop
# user-defined functions

# Python program to find factors of a number

def print_factors(x):
    """This function takes a
    number and prints the factors"""

    print("The factors of", x, "are: ")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

# take input from the user
num = int(input("Enter a number: ")) 

print_factors(num)

"""
In this program we take a number from the user and display its factors using the function
print_factors(). In the function, we use for loop to iterate from 1 to that number and only
print it if, it perfectly divides our number. Here, print_factors() is a user-defined function.
"""
