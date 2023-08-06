"""
Dictionary comprehension is an elegant and concise way to create new dictionary fron an
iterable in Python. Dictionary comprehension consists of an expression pair(key:value)
followed by for statement inside curly braces {}. Here is an example to make a dictionary with
each item being a pair of a number and its square.
"""
squares = {x: x*x for x in range(6)}
print(squares)

