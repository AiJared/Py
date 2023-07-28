# Extended Assignment Operators
alpha = [1, 2, 3]
beta = alpha # an alia for alpha
beta += [4, 5] # extends the original list with two more elements
beta = beta + [6, 7] # reassigns beta to a new list [1, 2, 3, 4, 5, 6, 7]
print(alpha) # will be [1, 2, 3, 4, 5]

# The above example demonstrates the subtle difference between the list semantics for
# syntax beta += foo or beta =  beta + foo.
