"""
Dictionary comprehension is an elegant and concise way to create new dictionary fron an
iterable in Python. Dictionary comprehension consists of an expression pair(key:value)
followed by for statement inside curly braces {}. Here is an example to make a dictionary with
each item being a pair of a number and its square.
"""
squares = {x: x*x for x in range(6)}
print(squares)

"""The above code is equivalent to:"""

squares = {}
for x in range(6):
    squares[x] = x*x

"""
A dictionary comprehension can optionally contain more for or if statements. An optional if
statement can filter out items to form the new dictionary. Here are some examples to make
with only odd items.
"""
odd_squares = {x: x*x for x in range(11) if x%2 == 1}
print(odd_squares)