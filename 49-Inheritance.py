# INHERITANCE- allos new objects to take on the property of existing objects
class User():
    def sign_in(self):
        print('logged in')
    
class wizard(User):
    def __init__(self,name,power):
        self.name=name
        self.power=power
        
    def attack(self):
        print(f'attacking with power of {self.power}')
        
class Archer(User):
    def __init__(self,name,num_arrows):
        self.name=name
        self.num_arrows=num_arrows
        
    def attack(self):
        print(f'attacking with arrows: arrows left-{self.num_arrows}')
        
wizard1= wizard('merlin',50)
archer1=Archer('Robin',100)
print(wizard1.sign_in())
wizard1.attack()
archer1.attack()

#-------------------------------------------------------------------------------
# to check instance of a class we have an inbuilt function in python
# isinstance
print(isinstance(wizard1,User))
#----------------(instance(attribute),class)
# in python everything is an object...python inherits from base object class 'object'
# so it should iherit from object too...
print(isinstance(wizard,object))
# any common functionality can be ditched out by inheriting from object...
# the parent class is actually accepting Object as a parameter
# class User(Object)





     
