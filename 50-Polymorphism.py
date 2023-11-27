#Poly means many
#morphism means many forms
# here objects and classes can share same method name and these methods can act differently based on what object calls them
class User():
    def sign_in(self):
        print('logged in')
        
    def attack(self):
        print('do nothing')
    
class wizard(User):
    def __init__(self,name,power):
        self.name=name
        self.power=power
        
    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')
        
class Archer(User):
    def __init__(self,name,num_arrows):
        self.name=name
        self.num_arrows=num_arrows
        
    def attack(self):
        print(f'attacking with arrows: arrows left-{self.num_arrows}')
        
wizard1= wizard('merlin',50)
archer1=Archer('Robin',100) 
print(wizard1.attack())

# Here 'attack' function is used in both wizard and archer but is doing different work in both the functions...
print(wizard1.attack())
print(archer1.attack())

# We can also call them in few different ways...
# 1. by defining a function
def Player_attack(char):
    char.attack()
Player_attack(wizard1)
Player_attack(archer1)

# 2. for loop
for char in [wizard1,archer1]:
    char.attack()
    
# Lets say we want to have both user and wizard to run attack() method...
# What you can do is in class wizard after def attack(self) you can acll User.attack() and give it self-->attack(self)
# output-dono ki attack ki statements print ho jayengi one after the other...

    