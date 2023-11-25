# @classmethod-we can use this without instantiating any class
# jha b hi ye use krenge method vha attributes ko instantiate nhi krna padega...
class PlayerCharacter:
    membership=True
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def shout(self):
        print(f'my name is {self.name}')
        
   # @classmethod
   # def adding_things(cls,num1,num2):
    #    return num1+num2
# same as self 'cls' word should be written as default...
#print(PlayerCharacter.adding_things(2,3))

# we can also instantiate objects through classmethod
@classmethod
def adding_things(cls,num1,num2):
    return cls('teddy',num1+num2)
               #   name,age for playcharacter
               
Player3=PlayerCharacter.adding_things(2,3)
print(Player3.age)

#-----------------------------------------------------------------
# @static method-we dont have access to parameter as cls(cls ke liye access nhi hota)
def adding_things2(num1,num2):
    return ('teddy,num1,num2')

#BOTH THESE METHODS ARE CALLED ON THE CLASS WITHOUT INSTANTIATING IT...



