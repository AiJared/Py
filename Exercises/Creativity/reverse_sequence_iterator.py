class ReverseSequenceIterator:
    """A reverse iterator for Python's sequence types."""

    def __init__(self, sequence):
        self._seq = sequence            # keep a reference to the underlying data
        self._k = 0                    # will decrement to 10 on the first call to next

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k -= 1                    # advance to nex lowest index
        if self._k < len(self._seq):
            return (self._seq[self._k]) # return the data element
        else:
            raise StopIteration()       # there are no more elements
        
    def __reverseiter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self
    
i = ReverseSequenceIterator(10)
print(i)