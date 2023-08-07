"""
Iterators are everywhere in Python. They are elegantly implemented within for loops,
comprehesions, generators etc. but hidden in plain sight. Iterator in Python is simply an object
that can be iterated upon. An object which will return data, one element at a time.

Technically speaking, Python iterator object must implement two special methods, __iter__()
and __next__(), collectively called the iterator protocol.

An object is called iterable if we can get an iterator from it. Most of built-in containers in
Python like: list, tuple, string etc. are iterables. The iter() function (which in turn calls the
__iter__() method) returns an iterator from them.
"""

# Iterating through an Iterator in Python
"""
We use the next() method to manually iterate through all the items of an iterator. When we 
reach the end and there is no more data to be returned, it will raise StopIteration. Following is
an example.
"""
# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter() on that list
my_iter = iter(my_list)
print(my_iter)

# iterate through it using next()
print(next(my_iter))

# next(obj) is same as obj.__next__()
print(my_iter.__next__())
print(my_iter.__next__())
print(next(my_iter))
# print(next(my_iter))
# no more items left

"""
A more elegant way of automatically iterating is by using the for loop. Using this, we can iterate
over any object that can return an iterator, for example list, string, file etc.
"""
for element in my_list:
    print(element)