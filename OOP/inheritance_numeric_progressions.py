"""
As a second example of the use of inheritance, we develop a hierarchy of classes for
iterating number progressions. A "numeric progression" is a sequence of numbers,
where each number depends on one or more of the previous numbers. For example,
an "arithmetic progression" determines the next number by adding a fixed constant
to the previous value, and a "geometric progression" determines the next number 
by multiplying the previous value by a fixed constant. In general, a progression
requires a first value, and a way of identifying a new value based on one or more
previous values.

To maximize reusability of code, we develop a hierarchy of classes stemming
from a general base class that we name "Progression". Technically.,
the Progression class produces the progression of whole numbers: 0, 1, 2, ....
However, this class is designed to serve as the base class for other progression types
providing as much common functionality as possible, and thereby minimizing the
burden on the subclasses.


The constructor of the Progression class accepts a starting value for the progression
(0 by default), and initializes a data member, self._current, to that value.

The Progression class implements the conventions of a "Python iterator"
namely the special __next__ and __iter__ methods. If a user of
the class creates a progression as seq = Progression(), each call to nex(seq) will
return a subsequent element of the progression sequence. It would also be possible
to use a for-loop syntac, for value in seq:, although we notr that our default
progression is defined as an infinite sequence.

To better separate the mechanics of the iterator convention from the core logic
of adnacing the progression, our framework relies on a nonpublic method named
_advance to update the value of the self._current field. In the default implementation
,_advance adds one to the current value, but our intent is that subclasses will
override _advance to provide a different rule for computing the next entry.

For convenience, the Progression class alo provides a utility method, named
print_progression, that displays the next n values of the progression.
"""

class Progression:
    """Iterator producing a generic progression.
    
    Default iterator produces the whole numbers 0, 1, 2, ...
    """
    def __init__(self, start=0):
        """Initialize current to the first value of the progression."""
        self._current = start

    def _advance(self):
        """Update self._current to a new value.
        
        This should be overriden by a subclass to customize progression.

        By convention, if current is set to None, this designates the

        end of a finite progression.
        """
        self._current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        if self._current is None:       # our convention to end a progression
            raise StopIteration()
        else:
            answer = self._current      # record current values to return
            self._advance()             # advance to prepare for next time
            return answer
        
    def __iter__(self):
        """By convention,an iterator must return itself as an iterator."""
        return self
    
    def print_progression(self, n):
        """Print next n values of the progression."""
        print(''.join(str(next(self))for j in range(n)))

# An Arithmetic Progression Class

"""
Our first of a specialized progression is an arithmeric progression. While
the default progression increases its value by one in each step, an arithmetic
progression adds a fixed constant to one term of the progression to produce the next.
For example, using an increment of 4 for an arithmetuc progression that starts at 0
results in the sequence 0, 4, 8, 12,...,

The code below presents our implementation of an ArithmeticProgression 
class, which relies on Progression as its base class. The constructor for this new
class accepts both an increment value and a starting value as parameters, although
default values for each are provided. By our convention, ArithmeticProgression(4)
produces the sequence 0,4,6,12,..., and ArithmeticProgression(4, 1) produces
the sequence 1, 5, 9, 13,....

The body of the ArithmeticProgression constuctor calls the super constructor
to initialize the _current data member to the desired start value. Then it directly
established the new _increment data member for the arithmetic progression. The
only remaining detail in our implemetation is to override the _advance method so 
as to add the increment to the current value.
"""

class ArithmeticProgression(Progression):               # Inherit from Progression
    """Iterator producing an arithmetic progression."""
    def __init__(self, increment=1, start=0):
        """Create a new arithmetic progression.
        
        increment   the fixed constant to add each term (default 1)
        start       the first term of the progression (defaut 0)
        """
        super().__init__(start)                          # initialize base class
        self._increment = increment

    def _advance(self):             # overried inherited version
        """Update current value by adding the fixed increment."""
        self._current += self._increment

# A Geometric Progression Class

"""
Our second example of a specialized progression is a geometric progression, in
which each value is produced by multiplying the preceeding value by a fixed constant
known as the "base" of the geometric progression. The starting point of a geometric
progression is traditionally 1, rather than 0, because multiplying 0 by any 
factor results in 0. As an example, a geometric progression with base 2 proceeds as
1, 2, 4, 8, 16,....

The code below presents our implemetation of GeometricProgression
class. The constructor uses 2 as a default base 1 and as a default starting value, but
either of those can be varied using optional parameters.
"""

class GeometricProgression(Progression):        # inherit from Progression
    """Iterator producing a geometric progression."""

    def __init__(self, base=2, start=1):
        """Create a new geometric progression.
        
        base    the fixed constant multiplied to each term (default=2)
        start   the first term of the progression (default=1)
        """
        super().__init__(start)
        self._base = base

    def _advance(self):     # override inherited version
        """Update current value by multipying it by the base value."""
        self._current *= self._base

# A Fibonacci Progression Class

"""
As our final example, we demonstrate how to use our progression framework to
produce a "Fibonacci progression". Each value of a Fibonacci series is the
sum of the two most recent values. To begin the series, the first two values are
conventionally 0 and 1, leading to the Fibonacci series 0,1,1,2,3,5,8,... . More
generally, such a series can be generated from any two starting values. For example,
if we start with values 4 and 6, the series proceeds as 4,6,10,16,26,42,... .
"""

class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression."""

    def __init__(self, first=0, second=1):
        """Create a new fibonacci progression.
        
        first   the first term of the progression (default 0)
        second  the second term if the progression (default 1)
        """
        super().__init__(first)     # start progression at first
        self._prev = second - first # fictitious value preceding the first

    def _advance(self):
        """Update current value by taking sum of previous two."""
        self._prev, self._current = self._current, self._prev + self._current