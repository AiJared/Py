# when computing a sum with the syntax x + y in Python, the names x and y must
# have been previously associated with objects that serve as values; a NameError
# will be raised if no such definitions are found. The process of determining the
# value associated with an identifier is known as "name resolution".
# whenever an identifier is assigned to a value, that definition is made with a
# specific "scope". Top-level assignments are typically made in what is known as 
# "global" scope. Assignments made within the body of a function typically have scope
# that is "local" to that function call. Therefore an assignment, x = 5, within a function
# no effect on the identifier, x, in the broder scope.

# Each distict scope in Python is represented using an abstraction known as a "namespace".
# A namespace manages all identifiers that are currently defined in a given scope.

# Python implements a namespace with its own dictinary that maps each identifying string
# (e.g., "n") to its associated values. Python provides several ways to examine a given namespace.
# The function, dir, reports the names of the identifiers in a given namespace (i.e., keys of the dictionary),
# while the function, vars, return the full dictionary. By default, calls to dir() and vars() report on the most
# locally enclosing namespace in which they are executes.

# When an identifier is indicated in a command, Python searches a series of
# namespaces in the process of name resoltion. First, the most locally enclosing
# scope is searched for a given name. If not found there, the  next outer scope is 
# searched, and so on.