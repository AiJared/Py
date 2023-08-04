"""
Scope of a variable is the portion of a program where the variable is recognized. Parameters and
variables defined inside a function is not visible from outside. Hence, they are a local scope.

Lifetime of a variable is the period throughout which the variable exists in the memory. The
lifetime of variables inside a function is as long as the function executes. They are destroyed
once we return from the function. Hence, a function does not remeber the value of a variable
from its previous calls.

Here is an example to illustrate the scope of a variable inside a function.
"""
def my_func():
    x = 10
    print("Value inside function:", x)

x = 20
my_func()
print("Value outside function:", x)

"""
Here, we can see that the value of x is 20 initially. Even though the function my_func() changed
the value of x to 10, it did not affect the value outside the function. This is because the variable x
inside the function is different (local to the function) from the one outside. Although they have
same names, they are two different variables with different scope.

On the other hand, variables outside the function are visible from inside. They have a global
scope. We can read these values from the inside the function but cannot change(write) them. In
order to modify the value of variables outside the function, they must be declared as global
variables using the keyword global.
"""