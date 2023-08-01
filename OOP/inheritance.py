"""
A hierarchical design is useful in software development, as common functionality
can be grouped at the most general level, thereby promoting reuse of code,
while differentiated behaviors can be viewd as extensions of the general case, In
object-oriented programming, the mechanism for a modular and hierachical organization
is a technique known as "inheritance". This allows a new class to be defined
based upon an existing class as the starting point. In object-oriented terminology,
the existing class is typically described as the "base class", "parent class", or "super
class", while the newly defined class is known as the "subclass" or "child class".

There are two ways in which a subclass can differentiate itself from its 
superclass. A subclass may "specialize" an existing behavior by providing a new
implementation and "overrides" an exisiting method. A subclass may also "extend" its
superclass by providing brand new methods.
"""

# Python's Exception Hierarchy

"""
Another example of a rich inheritance hierarchy is the organization of various
exception types in Python. The BaseException class is the root of the entire hierarchy,
while the more specific Exception class includes most of the error types that
we have discussed. Programmers are welcome to define their own special exception
classes to denote errors that may occur in the context of their application. Those
user-defined exception types should be declared as subclasses of Exception
"""

# Extending the CreditCard Class

"""
To demonstrate the mechanisms for inheritance in Python, we revisit the CreditCard
class, implementing a subclass that, for lack of a better name, we
name PredatoryCreditCard. The new class will differ from the original in two
ways: (1) if an attempted charge is rejected because it would have exceeded the
credit limit, a $5 fee will be charged and (2) there will be a mechanism for assessing
a monthly interest charge on the outstanding balance, based up on Annual
Percentage Rate(APR) specified as a constructor parameter.

In accomplishing this goal, we demonstrate the techbique of specialization
and extension. To charge a fee for an invalid charge attempt, we "override" the
existing charge methods, thereby specializing it to provide the new functionality
(although the new version takes advantage of a call to the overridden version). To
provide support for charging interest, we extend the class with a new method named
process_month
"""
class CreditCard:
    """A consumer credit card"""

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance
        
        The initial balance is zero.

        customer    the name of the customer(e.g., "John Bowman")
        bank        the name of the bank(e.g., "California Savings")
        acnt        the acount identifier(e.g., "5391 0375 9387 5309")
        limit       credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer
    
    def get_bank(self):
        """Return the bank's name."""
        return self._bank
    
    def get_account(self):
        """Return the card identifying number(typically stored as a string)."""
        return self._account
    
    def get_limit(self):
        """Return current credit limit."""
        return self._limit
    
    def get_balance(self):
        """Return current balance."""
        return self._balance
    
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
        
        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit: # if charge would exceed limit
            return False
        else:
            self._balance += price
            return True
        
    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount

"""
To indicate that the new class inherits from the existing CreditCard class, our
definition begins with the syntax class PredatoryCreditCard(CreditCard). The body of
the new class provides three member functions: __init__, charge, and process_month. The 
__init__ constructor serves a very similar role to the original
CreditCard constructor, except that for our new class, there is an extra parameter
to specify the annual percentage rate. The body of our new constructor relies upon
making a call to the inherited constructor to perform most of the initialization (in
fact, everything other than the recording of the percentage rate). The mechanism
for calling the inherited constructor relies on the syntac, super().
"""

# super().__init__(customer, bank, acnt, limit)

"""
calls the __init__ method that was inherited from the CreditCard superclass. Note
well that this method only accepts four parameters. We record the APR value in a
new field named _apr.

In similar fashion, our PredatoryCreditCard class provides a new implementation 
of the charge method that overides the inherited method. Yet, our
implementation of the new method relies on a call to the inherited method, with syntax
super().charge(price). The return value of that call designates whether
the charge was successful. We examine that return value to decide whether to assess
a fee, and in turn we return that value to the caller of method, so that the
new version of charge has a similar outward interface as the original.

The process_month method is a new behavior, so there is no inherited version
upon which to rely. In our model, this method should be invokdes by the bank, 
once each month, to add new interest charges o the customer's balance. The most
challenging aspect in implementating this method is making sure we have working
knowledge of how an annual rate translates to a monthly rate. We do
not simply divide by twelve to get a monthly rate (that would be too
predatory as it would result in a higher APR tha advertised). The correct computation
is to take the twelfth-root of 1 + self._apr and use that multiplication
factor. For example, if the APR is 0.0825 interest per month, we compute
12th-root of 1.0825 which is close to 1.006628, and therefore charge 0.6628 interest
per month. In this way, each $100 of debt will amass $8.25 of compounded interest in a year.
"""

class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""
    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance
        The initial balance is zero

        customer    the name of the consumer(e.g., 'John Bowman')
        bank        the name of the bank(e.g., 'California Savings')
        acnt        the account identifier(e.g., '5391 0375 5309')
        limit       credit limit (measured in dollars)
        apr         annual percentage rate(e.g., 0.0825 for 8.25% APR)

        """