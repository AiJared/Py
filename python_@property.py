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
