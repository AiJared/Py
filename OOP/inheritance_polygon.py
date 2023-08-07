class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side", i+1, "is", self.sides[i])

"""
This class has data attributes to store the number of sides, n and magnitude of each side as a list,
sides. Method inputSides() takes in magnitude of each side and similarly, dispSides() will
display these properly.

A triangle is a polygon with 3 sides. So we can create a class called Triangle which inherits
from Polygon. This makes all the attributes available in class Polygon readily available in
Triangle. We do not need to define them again (code re-usability). Triangle is defined as follows.
"""
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print("The area of the triangle is %0.2f" %area)

"""
However, class Triangle has a new method findArea() to find and print the area of the
triangle.
"""
t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()