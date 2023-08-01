"""
A hierarchical design is useful in software development, as common functionality
can be grouped at the most general level, thereby promoting reuse of code,
while differentiated behaviors can be viewd as extensions of the general case, In
object-oriented programming, the mechanism for a modular and hierachical organization
is a technique known as "inheritance". This allows a new class to be defined
based upon an existing class as the starting point. In object-oriented terminology,
the existing class is typically described as the "base class", "parent class", or "super
class", while the newly defined class is known as the "subclass" or "child class".

There are two ways in which a subclass can differentiate itself from its 
superclass. A subclass may "specialize" an existing behavior by providing a new
implementation and "overrides" an exisiting method. A subclass may also "extend" its
superclass by providing brand new methods.
"""

# Python's Exception Hierarchy

"""
Another example of a rich inheritance hierarchy is the organization of various
exception types in Python. The BaseException class is the root of the entire hierarchy,
while the more specific Exception class includes most of the error types that
we have discussed. Programmers are welcome to define their own special exception
classes to denote errors that may occur in the context of their application. Those
user-defined exception types should be declared as subclasses of Exception
"""

