# Built-in Functions
"""
ASCII stands for American Standard Code for Information Interchange. It is a numeric value
given to different characters and symbols, for computers to store and manipulate. For example:
ASCII value of letter 'A' is 65.
"""

# Take character from user
c = input("Enter a character: ")

print("The ASCII value of '" + c + "' is", ord(c))

"""
Here, we have used ord() function to convert a character to an integer (ASCII value). This
function actually returns the Unicode code point of that character. Unicode is also an encoding
technique that provides a unique number to a character. While ASCII only encodes 128
characters, current Unicode has more tha 100,000 characters from hundreds of scripts.

We can use chr() function to inverse the process, meaning return a character for the input integer
"""
print(chr(65))