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

