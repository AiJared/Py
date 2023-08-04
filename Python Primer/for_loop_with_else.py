"""
A for loop can have an optional else as well. The else part is executed if the items in the
sequence used in for loop exhausts. break statement can be used to stop a for loop. In such
case, the else part is ignored. Hence, a for loop's else part runs if no break occurs.

Here is an example to illustrate.
"""

# a list of digit
list_of_digits = [0, 1, 2, 3, 4, 5, 6]

# take input from the user
input_digit = int(input("Enter a digit: "))

# search the input digit in our list
for i in list_of_digits:
    if input_digit == i:
        print("Digit is in the list")
        break
else:
    print("Digit not found in the list")
