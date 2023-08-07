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
        self.imag = i

    def getData(self):
        print("{0} + {1}j".format(self.real, self.imag)) 

"""
In the above example, we define a new class to represent complex numbers. It has two functions,
__init__() to initialize the variables (defaults to zero) and getData() to display the number
properly.
"""    
c1 = ComplexNumbers(2, 3)
c1.getData()

c2 = ComplexNumbers(5)
c2.attr = 10
print(c2.real, c2.imag, c2.attr)
c2.getData()

"""
An interesting thing to note in the above step is that attributes of an object can be created on the
fly. We created a new attribute attr for object c2 and we read it as well. But this did not create
that attribute for object c1.
"""

# Deleting Attributes and Objects
"""
Any attribute of an object can be deleted anytime, using the del statement.
"""
c1 = ComplexNumbers(2, 3)
del c1.imag
c1.getData()

del ComplexNumbers.getData
c1.getData()

"""We can even delete the object itself using the del statement."""
c1 = ComplexNumbers(1, 3)
del c1

"""
Actually, it is more complicated than that. When we do c1 = CompexNumber(1, 3). a new
instance object is created in memory and the name c1 binds with it. On the command del c1,
this binding id removed and the name c1 is deleted from the corresponding namespace. The
object however continues to exist in memory and if no other name is bound to it, it is later
automatically destroyed. This automatic destruction of unreferenced objects in Python is also
called garbage collection.
"""