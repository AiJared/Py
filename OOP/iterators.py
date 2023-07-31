"""
An 'iterator' for a collection provides one key behavior: It supports a special method named __next__
that returns the next element of the collection, any, or raises a StopIteration exception 
to indicate that there are no further elements.

Fortunately, it is rare to habe to directly implement an iterator class. Our preferred approach
is the use of the 'generator' syntax which automatically produces an iterator yielded values.
"""

"""
Python also helps by providing an automatic iterator implementation for any class
that defines both __len__ and __getititem__. To provide an instructive example of 
a low-level iterator, the code below demonstrates just such an interior class that
works on any collection that supports both __len__ and __getitem__. 
This class can be instantiated as SequenceIterator(data). It operates by keeping an
internal reference to the data sequence, as well as a current index into the sequence.
Each time __next__ is called, the index is incremented, until reaching the end of the
sequence.
"""

class SequenceIterator:
    """An iterator for any of Python's sequence types."""

    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence    # keep a refrence to the underlying data
        self._k  = - 1          # will increment to 0 on first call to next

    def __next__(self):
        """Return the next element, or else raise stopIteration error."""
        self._k += 1    # advance to next index
        if self._k < len(self._seq):
            return (self._seq[self._k]) # return the data element
        else:
            raise StopIteration()   # there are no more elements
        
    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self