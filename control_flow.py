# Nest one control structure within another, relying on indentation to
# make clear the extent of the various bodies.
door_is_open = ""
door_is_closed = ""
door_is_locked = ""

def open_door():
    pass

def unlock_door():
    pass

def advance():
    pass

if door_is_closed:
    if door_is_locked:
        unlock_door()
    open_door()
advance()

# while loop
data = []
j = 0
while j < len(data) and data[j] != "X":
    j += 1

# For loops
total = 0
for val in data:
    total += val # note use of the loop variable val


biggest = data = [0] # as we assume nonempty list
for val in data:
    if val > biggest:
        biggest = val

# we can use a for loop in cases for which a while loop does not
# apply, such as when iterating through a collection of, such as
# a set, that does not support any direct form of indexing

# Index-Based For Loops

# In some applications, we need knowledge of the index of an
# element within the sequence. For example, suppose that we need
# to know where the maximum element in a list resied.

# Rather than directly looping over the elements of the list in that case,
# we prefer to loop over all possible indices of the list.
# For this purpose, Python provides a built-in class called "range"
# that generates "integer sequences".

big_index = 0
for j in range(len(data)):
    if data[j] > data[big_index]:
        big_index = j

# Break and Continue Statements

# "break" statement terminates a while or for loop when executed within its body.

target = ""
found = False
for item in data:
    if item == target:
        found = True
        break

# Python also supports a "continue" statement that causes the current "iteration" of a
# loop body to stop, but with subsequent passes of the loop proceeding as expected.
