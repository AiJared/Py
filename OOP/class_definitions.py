"""
A "class" serves as a primary means fir abstracting in object-oriented programming.
In Python, every piece of data is represented as an instance of some class.
A class provides a set of behaviors in the form of "member functions" (also known
as "methods"), with implementations that are common to all instances of that class.
A class also serves as a blueprint for its instances, effectively the way
that state information for each instance is represented in the form of "attributes" (also
known as "fields", "instance variables" or "data members).
"""

# Example: CreditCard Class

"""
The instances defined by the CreditCard class provide a simple model for traditional
credit cards. They have identifying information about the customer, bank, account number, 
credit limit and current balance. The class restricts charges that would cause a card's 
balance to go over its spending limit, but it does not charge interest or late payments.

In a class there are methods defined as functions which have a special parameter namesd
"self", that serves to identify the particular instance upon which a member is invoked
"""

# The self Identifier

"""
In Python, the self identifier plays a key role. In the context of CreditCard
class, there can presumably be many different CreditCard instances, and each must
maintain its own balance, its own credit limit and so on. Therefore, each instance
stores its own instances variables to reflect its current state.

Syntactically, self identifies the instance upon which a method is invoked. For
example, assume that a user of our class has a variable, my_card, that identifies
an instance of the CreditCard class. When the use calls my_card.get_balance(),
the identifier self, within the definition of the get_balance method refers to the card
known as my_card by the caller. The expressionm self._balance refers to an instance
variable, names _balance stored as part of that particular credit card'state.
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
We draw attention to the difference between the method signature as declared
within the class versus that used by a caller. For example, from a user's perspective
we have seen that the get_balance method takes zero parameters, yet within
the class definition, self is an explicit parameter. Likewise, the charge method is
declared within the class having two parameters(self and price), even though this
method is called with one parameter, for example, as my_card.charge(200). The
interpretter automatically binds the instance upon which the method is invoked to
the self parameter.
"""

# The Constructor

"""
A user can create an instance of the CreditCard class using a syntax as:
"""
cc = CreditCard("John Doe", "1st Bank", "5391 0375 9387 5309", 1000)
"""
Internally, this results in a call to the specially named __init__ method that serves
as the "constructor" of the class.. Its primary responsibility is to establish the state of
a newly created credit card object with appropriate instance variables. In the case
of the CreditCard class, each object maintains five instance variables, which we name:
_customer, _bank, _account, _limit, and _balance.
The initial values for the first four of those five are provided as explicit parameters that are
sent by the user when instantiating the credit card, and assigned within the body of the constructor
For example, the command, self._customer = customer, assigns the instance variable self._customer to
the parameter customer; note that because customer is variable self._customer to the parameter customer;
note that because customer is "unqualified" on the right-hand side, it refers to the parameter in the 
local namespace.
"""

# Testing the Class

"""
In the code below we demonstrate some basic usage of the CreditClass,
inserting three cards into a list named wallet. We use loops to make some charges
and payments, and use various accessors to print results to the console.

These tests are eclosed within a conditional, if__name__==__main__:,
so that they can be embedded in the source code with the class definition.
These tests provide "method coverage", as each of the methods is called at least
once, but it does not provide "statement coverage", as there is never a case in which
a charge is rejected due to the credit limit. This is not particularly advanced
from testing as the output of the given tests must be manually audited in order to determine
whether the class behaved as expected. Python has tools for more formal testing so that
resulting values can be automatically compared to the predicted outcomes, with output
generated only when an error is detected.
"""
if __name__ == "__main__":
    wallet = []
    wallet.append(CreditCard("John Bowman", "California Savings",
                             '5391 0375 9387 5309', 2500))
    wallet.append(CreditCard("John Bowman", "California Federal",
                             '3485 0399 3395 1954', 3500))
    wallet.append(CreditCard("John Bowman", "California Finance",
                             "5391 0375 9387 5309", 5000))
    
    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print("Customer = ", wallet[c].get_customer())
        print("Bank = ", wallet[c].get_bank())
        print("Account = ", wallet[c].get_account())
        print("Limit = ", wallet[c].get_limit())
        print("Balance = ", wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print("New balance = ", wallet[c].get_balance())
        print()