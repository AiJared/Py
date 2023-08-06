"""
Set is an unordered collection of items. Every element is unique(no duplicates) and must be 
immutable. However, the set itsetf is mutable (we can add or remove items). Sets can be used to
perform mathematical set operations like union, intersection, symmetric difference etc.
"""

# Creating a Set in Python
"""
A set is created by placing all the items (elements) inside curly braces {}, separated by comma or
by using the built-in function set(). It can have any number of items and they may be of 
different types (integer, float, tuple, string etc.). But a set cannot have a mutable element, like
list, set or dictionary, as its element.
"""
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# set from a list
a = set([1, 2, 3])
print(a)

"""
Creating an empty set is a bit tricky. Empty curly braces {} will make an empy dictionary in
Python. To make a set without any elements we use the set() method without any argument.
"""
i = set()
print(type(a))

# Changing a set in Python
"""
Sets are mutable. But since they are unordered, indexing have no meaning. We cannot access or
change an element of set using indexing or slicing. Set does not support it. We can add single
elements using the method add(). Multiple elements can be added using update() method. The
update() method can take tuples, lists, strings or other sets as its arguments. In all cases,
duplicates are avoided.
"""
my_set = {1, 3}
my_set.add(2)
print(my_set)

my_set.update([2, 3, 4])
print(my_set)

my_set.update([4, 5], {1, 6, 8})
print(my_set)

# Removing Elements from a Set

"""
A particular item can be removed from set using methods like discard(), and remove(). The
only difference between the two is that, while using discard() if item does not exist in the
set, it remains unchanged. But remove() will raise an error in such condition.
"""
my_set = {1, 3, 4, 5, 6}
my_set.discard(4)
print(my_set)
my_set.remove(6)
print(my_set)

"""
Similarly, we can remove and return an item using the pop() method. Set being unorderd, there
is no way of determining which item will be popped. It is compeletely arbitrary. We can also 
remove all items of a set using clear(). 
"""

# Python Set Operation
"""
Sets can be used to carry out mathematical set operations like union, intersection, difference and
symmetric difference. We can do this with operators or methods. Let us consider the following
two sets for the following operations.
"""
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Set Union
"""
Union of A and B is a set of all elements from both sets. Union is performed using | operator.
Same can be done using the method union()
"""
C = A | B
print(C)

C = A.union(B)
print(C)

C = B.union(A)
print(C)

# Set Intersection
"""
Intersectio of A and B is a set of elements that are common in both sets. Intersection is
performed using & operator. Same can be accomplished using the method intersection().
"""
D = A & B
print(D)

D = A.intersection(B)
print(D)

D = B.intersection(A)
print(D)

# Set Difference
"""
Difference of A and B (A-B) is a set of elements that are only in A but in B. Similarly, B-A
is a set of elements that are in B but not in A. Difference is permed using - operator. Same can be
accomplished using the method difference()
"""

E = A - B
print(E)

E = A.difference(B)
print(E)

F = B.difference(A)
print(F)

# Set Symmetric Difference
"""
Symmetric Difference of A and B is a set of element in both A and B except those common in
both. Symmetric difference is performed using ^ operator. Same can be accomplished using the
method symmetric_difference()
"""
G = A ^ B
print(G)
G = A.symmetric_difference(B)
print(G)
