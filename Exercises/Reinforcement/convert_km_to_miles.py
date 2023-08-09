# Program to convert kilometers to miles
# Input is provided by the user in kilometers

# take input from the user
kilometers = float(input("How many kilometers?: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print("%0.3f kilometers is equal to %0.3f miles" %(kilometers, miles))

"""
In this program, we use the ask the user for kilometers and convert it to miles by multipying it
with the conversion factor. With a slight modification, we can convert miles to kilometers. We
ask for miles and use the following formula to convert it into kilometers.
"""
