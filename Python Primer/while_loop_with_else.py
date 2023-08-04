"""
Same as thay of for loop, we can have an optional else block with while loop as well. The else
part is executed if the condition in the while loop evaluates to False. while loop can be
terminated with a break statement. In such a case, the else part is ignored. Hense, a while loop's
else part runs if no break occurs and the condition is false.

Here is an example
"""
counter = 0

while counter < 3:
    print("Inside loop")
    counter += 1
else:
    print("Inside else")

"""
Here, we use a counter variable to print the string "Inside loop" three times. On the fourth
iteration, the condition in while becomes False. Hence, the else part is executed.
"""