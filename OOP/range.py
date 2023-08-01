"""
Range is a class that can effectively represent the desired range of elements without ever
storing them explicitly in memory. To better explore the built-in range class, we recommend
that you create an instance as:
"""
r = range(8, 140, 5)

"""
The result is a relatively lightweight object, an instance of the range class that has only a few
behaviors. The syntax
"""
len(r)

"""
will report the number of elements that are in the given range(27, in our example). A range also supports
the __getitem__ method, so that syntax r[15] reports the sixteenth element in the range (as r[0] is the first
element). Because the class supports both __len__ and __getitem__, it inherits 
automatic support for iteration which is why it is possible to execute a for loop over range.

At this point we are ready to demonstrate our own version of such a class. The code below
provides a class we name Range(so as to clearly differentiate it from
built-in range). The biggest challenge in the implemetation is properly computing
the number of elements that belong in the range, given the parameters sent by the
caller when constructing a range. By computing that value in the constructor, and 
storing it as self._length, it becomes trivial to return it from the __len__ method. To
properly implement a call to __getitem__(k), we simply take the starting value of
the range plus k times the step size(i.e., for k=0, we return the start value). There
are a few subtleties worth examining in the code:

    - To properly support optional parameters, we rely on the technique describes
      when discussing a functional version of range
    - We compute the number of elements in the range as
      max(0, (stop - start + step -1) // step)
      It is worth testing this formula for both positive and negative step sizes
    - The __getitem__ method properly supports negative indices by converting
      an index -k to len(self) - k before computing the result.  
"""