"""
Class functions that begins with double underscore(__) are called special functions as they habe
special meaning. Of one particular interest is the __init__() function. This special function gets
called whenever a new object of that class is instantiated. This type of function in called
a constructor in Object Oriented Programming(OOP). We normally use it to initialize all the
variables.
"""
class ComplexNumbers:
    def __init__(self, r = 0, i = 0):
        self.real = r
        self.image = i

    def getData(self):
        print("{0} + {1}j".format(self.real, self.image)) 

"""
In the above example, we define a new class to represent complex numbers. It has two functions,
__init__() to initialize the variables (defaults to zero) and getData() to display the number
properly.
"""    
c1 = ComplexNumbers(2, 3)
c1.getData()

c2 = ComplexNumbers(5)
c2.attr = 10
print(c2.real, c2.image, c2.attr)
c2.getData()

"""
An interesting thing to note in the above step is that attributes of an object can be created on the
fly. We created a new attribute attr for object c2 and we read it as well. But this did not create
that attribute for object c1.
"""