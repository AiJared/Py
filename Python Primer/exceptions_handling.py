"""
When an exception occurs in Python, it causes the current process to stop and passes it to the
calling process unitl it is handled. If not handled, our program willc crash. For example, if
function A calls function B which in turn calls function C and an exception occurs in function C. If
it is not handled in C, the exception passes to B then to A. If never handled, an error message
is spit out and our program come to a sudden, unexpected halt.
"""

# Catching Exceptions in Python

"""
In Python, exceptions can be handled using try statement. A critical operation which can raise
exception is placed inside the try clause and the code that handles exception is written in
except clause. It is up to us, what operations we perform once we have caught the exception.
Here is a simple example.
"""
import sys

while True:
    try:
        x = int(input("Enter an integer: "))
        r = 1/x
        break
    except:
        print("Oops!", sys.exc_info()[0], "occured.")
        print("Please try again.")
        print()

print("The reciporcal of", x, "is", r)