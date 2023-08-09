# Three sides of the triangle are provided by the user
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of the triangle is %0.2f" %area)

"""
In this program, we asked the user ti enter the length of three sides of a triangle. We used the
Heroin's formula to calculate the semi-perimeter and hence the area of the triangle.
"""
