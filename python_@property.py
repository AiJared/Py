"""
Python has a great concept called property, which makes the life of an object oriented
programmer much simpler. Before defining and going into details of what a property in Python
is, let us first build an intuition on why it would be needed in the first place.
"""
# An Example to Begin With
"""
Let us assume that one day you decide to make a class that could store the temperature in degree
Celcius. It would also implement a method to convert the tempereture into degree Fahrenheit.
One way of doing this is as follows.
"""
class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

"""
We could make objects out of this class and manipulate the attribute temperature as we
wished.
"""
# create new object
man = Celsius()

# set temperature
man.temperature = 37

# get temperature
print(man.temperature)

# get degrees Fahrenheit
print(man.to_fahrenheit())

"""
The extra decimal places when converting into Fahrenheit is due to the floating point arithmetic
error(try 1.1 + 2.2 in Python interpreter). Whenever we assign or retrieve any object attribute
like temprature, as shown above, Python searches it in the object's __dict__ dictionary.
"""
print(man.__dict__)

"""
Therefore, man.temperature internally becomes man.__dict__['temperature'].

Now, let's further assume that our class got popular among clients and they started using it in
their programs. They did all kinds of assignments to the object. One faithful day, a trusted client
came to us and suggested that temperatures cannot go below -273 degree Celsius (students of
thermodynamics might argue that its actaully -273.15), also called absolute zero. He further
asked us to implement this value constraint. Being a comapny that strive for customer
satisfaction, we heeded the suggestion and released version 1.01, an upgrade of our
existing class.
"""
# Using Getters and Setters

"""
An obvious solution to the above constraint will be to hide the attribute temperature (make it
private) and define new getter and setter interfaces to manipulate it. This can be done as follows.
"""
class Celsius:
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32
    
    # new update
    def get_temperature(self):
        return self._temperature
    
    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

"""
We can see that new methods get_temperature() and set_temperatures() were
defined and furthermore, temperature was replaced wih _temperature. An underscore(_)at
the beginning is used to denote protected variables in Python.
"""
# c = Celsius(-277)
# print(c)

c = Celsius(37)
print(c.get_temperature())
c.set_temperature(10)
# c.set_temperature(-300)
"""
The big problem with the above update is that, all the clients
who implemented our previous class in their program have to modify theier code from
obj.temperature to obj.get_temperature() and all assignments like obj.temperature = 
val to obj.set_temperature(val). This refactoring can cause headaches to the clients with
hundreds of thousands of lines of codes.

All in all, our new update was not backward compatible. This is why property comes to rescue.
"""
