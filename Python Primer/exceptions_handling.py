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

# Raising Exceptions
"""
In Python programming, exceptions are raised when corresponding errors occur at run time, but
we can forcefully raise it using the keyword raise. We can also optionally pass in value to the
exception to clarify why that exception was raised.
"""
try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive integer!")
except ValueError as ve:
    print(ve)

# try...finally
"""
The try statement in Python can have an optional finally clause. This clause is executed no
matter what, and is generally used to release external resources. For example, we may be 
connected to a remote data center through the network or working with a file or working with a
Graphical User Interface (GUI). In all these circumstances, we must clean up the resources once
used, whether it was successful or not. These actions (closing a file, GUI or disconnecting from 
network) are performed in the finally clause to guarantee execution.
"""
try:
    f = open("test.txt", encoding="utf-8")
    # perform file operations
finally:
    f.close()

"""This type of construct makes sure the file is closed even if the exception occurs."""
