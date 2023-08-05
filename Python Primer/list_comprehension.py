"""
List comprehension is an elegant and concise way to create new list froman existing list in
Python. List comprehension consists of an expression followed by for statement inside square
brackets. Here is an example to make a list with each item being increasing power of 2
"""

pow2 = [2 ** x for x in range(10)]
print(pow2)

# the above code is equivalent to
pow2 = []

for x in range(10):
    pow2.append(2 ** x)

"""
A list comprehension can optionally contain more for or if statements. An optional if
statement can filter out items for the new list. Here are some examples.
"""
pow2 = [2 ** x for x in range(10) if x > 5]
print(pow2)

odd = [x for x in range(20) if x % 2 == 1]
print(odd)
