# Python provides integrated support for embedding formal documentation directly
# in source code using a mechanism known as a "docstring". Formally, any strinf literal
# that appears as the first statement within the body of a module, class, or function
# (including a member function of a class) will be considered to be a docstring. By 
# convention, those string literals whould be delimited within triple quotes ("""). As
# an example, our version of scale function could be documented
# as follows:
def scale(data, factor):
    """Multiply all entries of numeric data list by the given factor."""
    for j in range(len(data)):
        data[j] *= factor


"""
It is common to use tripple-quoted string delimiter for a docstring, even when
the string fits on a single line, as in the above example. More detailed docstrings
should begin with a single line that summarizes the purpose, followed by a blank
line, and then futher details. For example, we might more clearly document the
scale function as follows:
"""
def scale(data, factor):
    """Multiply all entries of numeric data list by the given factor.
    
    data    an instance of any mutable sequence type (such as a list)
            containing numeric elements
    
    factor  a number that serves as the multiplicative factor for scaling
    """
    for j in range(len(data)):
        data[j] *= factor

"""
A docstring is stores as a field of the module, function, or class in which it
is declared. It serves as documentation and can be retrieved in a variety of ways.
For example, the command help(x), within the Python interpreter, produces the
documentation associated with the identifier object x. An external tool named
'pydoc' is distributed with Pyton and can be used to generate formal documentation
as text or as a web page.
"""