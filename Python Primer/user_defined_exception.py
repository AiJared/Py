"""
Users can define their own exception by creating a new class in Python. This exception class has
to be derived, either directly or indirectly, from Exception class. Most of the built-in exceptions
are also derived fro this class
"""
class CustomError(Exception):
    pass

"""
Here, we have created a user-defined exception called CustomError which is derived from the
Exception class. This new exception can be raised, like other exceptions, using the raise
statement with an optional error message.

When we are developing a large Python program, it is a good practice to place all the user-
defined exceptions that our program raises in a separate file. Many standard modules do this.
They define their exceptions separately as exceptions.py or errors.py (generally but not
always).

User-defined exception class can implement everything a normal class can do, but we generally
make them simple and concise. Most implementatioons declare a custom base class and derive
other exception classes from this base class. This concept is made clearer in the following
example.

The program below will ask the user to enter a number until they guess a stored
number correctly. To help them figure it out, hint is provided whether their guess is greater than
or less than the stored number.
"""
# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions."""
    pass

class ValueTooSmallError(Error):
    """Raised when input value is too small"""
    pass

class ValueTooLargeError(Error):
    """Raised when input value is too large"""
    pass

# our main program
# user guesses a number until he/she gets it right

# you need to guess this number
number = 10

while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")

    except ValueTooLargeError:
        print("This value is too large, try again!")

print("Congratulations! You guessed it correctly.")
