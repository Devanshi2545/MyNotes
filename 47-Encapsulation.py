# 4 pillars of OOPS
# 1. ENCAPSULATION-Binging of data and functions that manipulate that data and we encapsulate everything in one box so that code or other machine can work in...
# Data and Functions are attributes and methods

# Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
# It describes the idea of wrapping data and the methods that work on data within one unit. 
# This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. 
# To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variables.

# A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc. 
# The goal of information hiding is to ensure that an object’s state is always valid by controlling access to attributes that are hidden from the outside world.

# Consider a real-life example of encapsulation, in a company, there are different sections like the accounts section, finance section, sales section etc. 
# The finance section handles all the financial transactions and keeps records of all the data related to finance. Similarly, the sales section handles all the sales-related activities and keeps records of all the sales.
# Now there may arise a situation when due to some reason an official from the finance section needs all the data about sales in a particular month. In this case, he is not allowed to directly access the data of the sales section. 
# He will first have to contact some other officer in the sales section and then request him to give the particular data. This is what encapsulation is. Here the data of the sales section and the employees that can manipulate them are wrapped under a single name “sales section”.
# Using encapsulation also hides the data. In this example, the data of the sections like sales, finance, or accounts are hidden from any other section.

# ACTIONS AND METHODS ARE USEFUL IN ENCAPSULATION BECAUSE IF THERE WILL BE NO METHODS BUT ONLY ATTRIBUTES IT WOULD BE LIKE A DICTIONARY...
#WITH ENCAPSULATION
class PlayerCharacter:
    membership=True
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def run(self):
        print('run')
        
    def speak(self):
        print(f'my name is {self.name}, and i am {self.age} years old.')
        
player1=PlayerCharacter('devanshi',21)
print(player1)

#-----------------------------------------------------------------------------------
# without ENCAPSULATION as we made a dictionary and use it
player2={'name':'Devanshi','age':21}
print(player2['name'])
print(player2['age'])

# Using ENC. and combining things into instances can  be useful because our world is full of data and it makes some sense...


        
        

        
