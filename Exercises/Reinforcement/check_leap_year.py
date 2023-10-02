# Python operators
# Python if...elif...else and Nested if

year = int(input("Enter a year: "))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year)) 

"""
In this program, we ask the user to input a year and check if it s leap year or not. Leap years
are those divisible by 4. Except those that are divisible by 100 but not 400. Thus 1900 is not a 
leap year as it is divisible by 100 but 2000 is a leap year because it is divisible by 400 as well
"""  
