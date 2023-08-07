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

# Method Overriding
"""
In the above example, notice that __init__(), method was defined in both classes, Triangle as
well as in Polygon. when this happens, the method in the derived class overrides that in the base
class. This is to say, __init__() in Triangle gets preference over the same in Polygon.
Generally when overriding a base method, we tend to extend the definition rather than simply
replace it. The same is being done by calling the method in base class from the one in derived
class (calling Polygon.__init__() from __init__() in Triangle). A better option would be
to use the built-in function super(). So, super().__init__(3) is equivalent to
Polygon.__init__(self, 3) and is preferred.

Two built-in functions isinstance() and issubclass() are used to check inheritances.
Function isintance() returns True if the object is an instance of the class or other classes
derived from it. Each and every class in Python inherits from the base class object.
"""

print(isinstance(t, Triangle))
print(isinstance(t, Polygon))
print(isinstance(t, int))
print(isinstance(t, object))

"""
Similarly, issubclass is used to check for class inheritance
"""
print(issubclass(Polygon, Triangle))
print(issubclass(Triangle, Polygon))
print(issubclass(bool, int))

# Python Multiple Inhertance
"""
A class can be derived from more than one base classes. The syntax for multiple inheritance is similar to
single inheritance.
"""
class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass

"""The class MultiDerived inherits from both Base1 and Base2"""

# Multilevel Inheritance in Python
"""
On the other hand we can inherit from a derived class. This is also called multilevel inheritance.
Multilevel inheritance can be of any depth in Python.
"""
class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Derived1):
    pass

