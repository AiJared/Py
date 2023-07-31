"""
In a 3-D space, we might wish to represent a vector with coordinated (5, -2, 3). Although it might be
tempting to directly use a Python list to represent those coordinates, a list does not provide an appropriate
abstraction for a geometric vector. In particular, if using lists, the expression[5, -2, 3] + [1, 4, 2]
results in the list [5, -2, 3, 1, 4, 2]. When working with vectors, if u = (5, -2, 3) and v = (1, 4, 2), ome would
expect the expression, u + v, to return a three-dimensional vector with coordinates (6, 2, 5).

We therefore define a vector class that providesd a better abstraction for the notion of a geometric vector. Internally, our
vector relies upon an instance of a list, named __coords, as its storage mechanism. By keeping the
internal list encapsulated, we can enforce the desired public interface for instances of our class.
A demonstration of supported behaviors includes the following":
"""
"""
v = Vecotor(5) # construct five-dimensional <0, 0, 0, 0, 0>
v[1] = 23      # <0, 23, 0, 0, 0> (based on use of __setitem__)
v[-1] = 45     # <0, 23, 0, 0, 45> (also via __setitem__)
print(v[4])    # print 45(via __getitem__)
u = v + v      # <0, 46, 0, 0, 90>
print(u)       # print <0, 46, 0, 0, 90>
total = 0
for entry in v:# implicit iteration via __len__ and __getitem))
    total += entry
"""
