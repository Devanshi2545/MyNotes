# Introspection-ability to determine type of object at runtime...
# 'dir()' in bracket we give that instance that we want to check...it will tell us the type of all the objects used in that instance
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

print(dir(wizard1))

