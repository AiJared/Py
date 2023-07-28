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

