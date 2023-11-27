# In Python, the super() function is used to refer to the parent class or superclass. It allows you to call methods defined in the superclass from the subclass, enabling you to extend and customize the functionality inherited from the parent class.
# say we had a function in parent class that has email as a parameter and we want to call that parameter in any subclass then we can do two things 1. to create the same parameter in subclass when there in __init__ method in parent class but we know 
# it will do enter the same parameter value in every class so we call __ini__ function in subclass or 2. is we can call super()
# it doesnt need self as a parameter...
# Example
class User():
    def __init__(self,email):
        self.email=email
    def sign_in(self):
        print('logged in')
    
class wizard(User):
    def __init__(self,name,power,email):
        User.__init__(self,email) #1 method
        super().__init__(email)   #2 method
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
        
wizard1= wizard('merlin',50,'merlin@gmail.com')
archer1=Archer('Robin',100)

print(wizard1.email)