# Python program to swap two variables provided by the user
x = input("Enter value of x: ")
y = input("Enter value of y: ")

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print("The value of x after swapping: {}".format(x))
print("The value of y after swapping: {}".format(y))

"""
In this program, we use the temp variable to temporarily hold the value of x. We then put the
value of y in x and later temp in y. In this way, the values get exhanged. 
"""
