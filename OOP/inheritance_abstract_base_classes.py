"""
When defining a group of classes as part of an inheritance hierarchy, one technique
for avoiding repetition of code is to design a base class with common functionality
that can be inherited by other classes that need it. As an example, the
hierarchy on Progression class, serves as a base
class for three distinct subclasses: ArithmeticProgression, GeometricProgression and
FibonacciProgression. Although it is possible to create an instance of the
Progression base class, there is little value in doing so because its behavior is simply
a special case of an ArithmeticProgression with increment 1. The real purpose
of the progression class was to centralize the implementation of behaviors that
progressions needed, thereby streamlining the code that is relegated to those
subclasses.

In classic object-oriented terminology, we say a class is an "abstract base class"
if its only purpose is to server as a base class through inheritance. More formally,
an abstract base class is one that cannot be direclty instantiated, while a "concrete
class" is one that can be instantiated. By this definition, our Progression class is
technically concrete, although we essentially designed it as an abstract base class.

Our reason for focusing on abstract base classes in our study of data structures
is that Python's collections module provides several abstract base classes that assist 
when defining custom data structures that share a common interface with of
Python's built-in data structures. These rely on an object-oriented softare design
pattern known as the "template method pattern". The template method pattern is
when an abstract class provides concrete behaviors that rely upon calls to
other abstract behaviors. In that way, as soon as a subclass provides definitions for
the missing abstract behaviors, the inherited concrete behaviors are well defined.

As a tangible example, "the collections.Sequence" abstract base class defines
behaviors common to Python's list, str, and tuple classes, as sequences that 
support element access via an integer index. More so, the collections.Sequence class
provides concrete implementations of methods, count, index, and __contains__
that can be inherited by any class that provides concrete implementations of both
__len__ and __getitem__. For the purpose of illustration, we provide a sample
implementation of such a Sequence abstract base class in the code below.
"""
from abc import ABCMeta, abstractmethod # need these definitions

class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class."""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence."""

    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j of the sequence."""

    def __contains__(self, val):
        """Return True if val found in the sequence; False otherwise."""
        for j in range(len(self)):
            if self[j] == val:          # found match
                return True
        return False
    
    def index(self, val):
        """Return leftmost index at which val is found (or raise ValueError)."""
        for j in range(len(self)):
            if self[j] == val:          # leftmost match
                return j
        raise ValueError('value not in response') # never found a match
    
    def count(self, val):
        """Return the number of elements equal to given value."""
        k = 0
        for j in range(len(self)):
            if self[j] == val:          # found a match
                k += 1
        return k
    
"""
The implementation relies on two advanced Python techniques. The first is that
we declare the ABCMeta class of the abc module as a "metaclass" of our Sequence
class. A metaclass is different from a superclass, in that it provides a template for
the class definition itself. Specifically, the ABCMeta declaration assures that the
constructor for the class raises an error.

The second advanced technique is the use of the @abstractmethod decorator
immediately before the __len__ and __getitem__ methods are declared. That
declares these two particular methods to be abstract, meaning that we do not provide
an implemetation within our Sequence base class, but that we expect any concrete
subclasses to support those two methods. Python enforces this exception, by disallowing
instantiation for any subclass that does not override the abstract methods
with concrete implementation.

The rest of the Sequence class definition provides tangible implementations for
other behaviors, under the assumption that the abstract __len__ and __getitem__
methods will exist in a concrete subclass. If you carefully examine the source code,
the implemetation of methods __contains__, index and count do not rely on any
assumption about the self instances, other than syntax len(self) and self[j] are
supported (by special methods __len__ and __getitem__, respectively). Support 
for iteration is automatic.

Finally, we emphasize that if a subclass provides its own implemetation of 
an inherited behavior from a base class, the new definition overrides the inherited
one. This technique can be used when we have the ability to provide a more efficient
implemetation for a behavior than is achieved by the generic approach. As
an example, the general implemetation of __contains__ for a sequence is based
on loop used to search for the desired value. For our Range class, there is an 
opportunity for a more efficient determination of containment. For example, it
is evident that the expression, 100000 in Range(0, 2000000, 100), should evaluate
to True, even without examining the individual elements of the range, because
the range include 100000, as that is a multiple of 100 that is between the start and 
stop values.
"""