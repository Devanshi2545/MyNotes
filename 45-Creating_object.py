class PlayerCharacter:
    def __init__(self,name,age):# init method or dunder method-it is called when anytime we instantiate
        self.name=name
        self.age=age
    def run(self):
        print('run')
        return'done'
        
player1=PlayerCharacter('Sandy',44)
player2=PlayerCharacter('Brad',43)

print(player1)
print(player2)
print(player1.name)
print(player2.name)
print(player1.age)
print(player2.age)

print(player1.run())

# here we used one piece of code and to create multiple players created from same blue print (ran to different outpute at different locations)
#output shows that we have a player character also it shows the memory location at which it is being located...
# OOP helps us write code that is:
# 1. repeatable
# 2. well organised
# 3. memory efficient


print(help(player1)) #shows the blue prinnt

print(list) #also shows blue print 

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#Class Object Attribute
#unlike other attributes ,this type of attribute remains static throughout the code...and are written from same line from where function starts

#other attributes we created in class are dynamic...
class PlayerCharacter:
    #class object attribute
    membership= True
    def __init__(self,name,age):
        if(self.membership):
         self.name=name
         self.age=age
    def shout(self):
        print(f'my name is {self.name}')
        
        
player1=PlayerCharacter('Sandy',44)
player2=PlayerCharacter('Brad',43)

print(player1.membership)
print(player2.membership)
print(player1.shout())
print(player2.shout())

            
            
# class object attribute doesnt change with instances
#----------------------------------------------------------------------
# init method or dunder method-it is called when anytime we instantiate
        #__init__ is a constructor function..is called everytime we instanciate an object
        #we can also use default parameters...
class PlayerCharacter:
    #class object attribute
    membership= True
    def __init__(self,name='anonymous',age=0):
        if(age>18):
         self.name=name
         self.age=age
    def shout(self):
        print(f'my name is {self.name}')
        
        
player1=PlayerCharacter('Sandy',40)
print(player1.shout())


        
    