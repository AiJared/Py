"""
We can have a if...elif...else statement inside another if...elif...else statement. This
is called nesting in computer programming. I fact, any number of these statements can be
nested inside one another. Indentation is the only way to figure out the level of nesting. This can
get confusing somtimes.
"""

# Python Nested if Example

# In this program we input a number
# check if the number is positive or
# negative or zero and display
# an appropriate message using nested if

num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("zero")
    else:
        print("Positive number")
else:
    print("Negative number")