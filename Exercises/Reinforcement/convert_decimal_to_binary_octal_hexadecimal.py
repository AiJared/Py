# Built-in functions

"""
Decimal system is the most widely used number system. But computer only understands binary.
Binary, octal and hexadecimal number system are closely related and we may require to convert
decimal into these systems. Decimal system is base 10 (ten symbols, 0-9, are used to represent a
number) and similarly, binary is base 2, octal is base 8 and hexadecimal is base 16.

A number with prefix '0b' is considered binary, '0o' is considered octal and '0x' as
hexadecimal For example

60 = 0b1110 = 0o74 = 0x3c
"""

# Python program to convert decimal number into binary, octal and hexadecimal number system

# take decimal number from user
dec = int(input("Enter an integer: "))
print("The decimal value of", dec, "is:")
print(bin(dec), 'in binary')
print(oct(dec), 'in octal')
print(hex(dec), 'in hexadecimal')

"""
In this program, we have used built-in functions bin(),oct() and hex() to convert the given
decimal number into respective number systems. These functions take an integer (in decimal)
and return a string.
"""