"""
We revisit the goal of finding the largest element of a
Python list;

Code Fragment 3.1 presents a function named find max for this task
"""

def find_max(data):
    """Return the maximum element from a nonempty Python list."""
    biggest = data[0]       # The initial value to beat
    for val in data:        # For each value:
        if val > biggest:   # If it is greater than the biggest so far,
            biggest = val   # We have found a new best (so far)
    return biggest          # When loop ends, biggest is the max

"""
This is a classic example of an algorithm with a running time that grows proportional
to n, as the loop executes once for each data element, with some fixes
number of primitive operations executing for each pass. In the remainder of this
section, we provide a framework to formalize this claim.
"""
