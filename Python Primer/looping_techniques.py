"""
Python offers two kinds of loop, the for loop and the while loop. Using these loops
along with loop control statements like break and continue, we can create various forms of
loop
"""

# The infinite loop

"""
We can create an infinite loop using while statement. If the condition of while loop is always
True, we get an infinite loop.
"""

# Example

# while True:
#     num = int(input("Enter an integer: "))
#     print("The double of", num, "is", 2 * num)

# Loop with condition at the top

"""
This is a normal while loop without break statements. The condition of the while loop is at the
top and the loop terminates when this condition is False.
"""

n = int(input("Enter n: "))

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i += 1

print("The sum is", sum)

# Loop with the condition in the middle

"""
This kind of loop can be implemented using an infinite loop along with a conditional break in
between the body of the loop.
"""

# take input from the user until a vowel is entered
vowels = "aeiouAEIOU"

# infinite loop
while True:
    v = input("Enter a vowel: ")

    # condition in the middle
    if v in vowels:
        break
    print("That is not a vowel. Try again!")
print("Thank you!")

# Loop with conition at the bottom

"""
This kind of loop ensures that the body of the loop is executed at least once. It can be
implemented using an infinite loop along with a condtional break at the end. This is similar to
the do...while loop in C.
"""

# Roll a dice until the user chooses to exit
import random

while True:
    input("Press enter to roll the dice")

    # get a number between 1 to 6
    num = random.randint(1,6)
    print("You got", num)
    option = input("Roll again? (y/n) ")

    # condition
    if option == "n":
        break
    