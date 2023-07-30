# The following function counts the number of occurences of a given target
# value within any form of iterable data set
print("Welcome to the GPA calculator.")
print("Please enter all your letter grades, one per line.")
print("Enter a blank line to designate the end.")
# map from letter grade to point value
points = {"A+": 4.0, "A": 4.0, "A-": 3.67, "B+": 3.33, "B": 3.0, "B-": 2.667,
          "C+": 2.33, "C":2.0, "C-":1.67, "D+": 1.33, "D": 1.0, "F": 0.0}
num_courses = 0
total_points = 0
done = False
while not done:
    grade = input()
    if grade == "":
        done = True
    elif grade not in points:
        print("Unkown grade '{0}' being ignored".format(grade))
    else:
        num_courses += 1
        total_points += points[grade]

    if num_courses > 0:
        print("Your GPA is {0:.3}".format(total_points / num_courses))


def count(data, target):
    n = 0
    for item in data:
        if item == target: # found a match
            n += 1
    return n

# Return Statement

# A "return" statement is used within the function body to indicate that the function
# should cease execution, and that an expressed values should be 
# returned to the caller.
# If a return statement is executed without an explicit argument,
# the None values is automatically returned. Likewise, None will be returned if
# the flow of control ever reaches the end of a function body without having executed
# a return statement.
def contains(data, target):
    for item in target:
        if item == target:
            return True
    return False

# Information Passing

# in the context of a "function signature", the identifiers used to describe the expected
# parameters are known as "formal parameters" and the objects sent by the caller
# when invoking the function are the "actual parameters"

# Parameter passing in Python follows the semantics of the standard "assignment statement".
# When a function is invoked, each identifier that serves as a formal parameter is assigned in
# function's local scope, to the respective actual parameter that is provided by the
# caller of the function. For example.
prizes = count(grade, "A")

# Just before the function body is executed, the actual parameters, grades and "A", 
# are implicitly assigned to the formal parameters, data and target as follows:
data = grade
target = "A"

# Mutable Parameters

# Python's parameter passing model has additional implications when a parameter is a mutable
# object. Because the formal parameter is an alias for the actual parameter,
# the body of the function may interact with the object in ways that change its state.
# Considering again our sample invocation of the count function, if the body of the function
# executes the command data.append("F"), the new entry is added to the
# end of the list identified as data within the function, which is one and the same as
# the list known on the caller as grades.

# There are many legitimate cases in which a function may be designed (and clearly documented) to
# modify the state of a parameter. As a concrete example, 
# we present the following implementation of a method named scale that's
# primary purpose is to multiply all entries of a numeric data set by a given factor.
def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor

# Default Parameter Values

# Python provides means for functions to support more than one possinle calling
# signature. Such a function is said to be "polymorphic" which is a Greek for "many forms".
# Most notably, functions can declare one or more default values for parameters, thereby
# allowing the caller to invoke a function with varying numbers of 
# actual parameters. For example

def compute_gpa(grades, points= {"A+": 4.0, "A": 4.0, "A-": 3.67, "B+": 3.33, "B": 3.0, "B-": 2.667,
          "C+": 2.33, "C":2.0, "C-":1.67, "D+": 1.33, "D": 1.0, "F": 0.0}):
    num_courses = 0
    total_points = 0
    for g in grades:
        if g in points:
            num_courses += 1
            total_points += points[g]
    return total_points / num_courses

# Keyword Parameters

# Python supports an alternate mechanism for sending a parameter to a funtion
# known as a "Keyword argument". A keyword argument is specified by explicitly
# assigning an actual parameter to a formal parameter by name. 
# For example foo(c=5)