# Abstraction- means hiding of information or abstracting information -- giving access of information that is necessary else hiding everything that is not needed by user...
# for ex
print((1,2,3,1).count(1))
# Here we just needed to count occurance of 1...how did it happend it not that really matter to he user ...he just wants tha aswer
# so here the method of counting at the backend is abstracted...
# sometimes all we need is a method and not to worry about how it is being implemented...
print(len((1,2,3,1)))
# here we dont need to know how length is being measured we just need the answer...
# we dont need to learn code of this from scratch

# EXAMPLE-Camera of an apple iphone we dont  need to know the code algorithm behind capturing photo we just want to click and have pictures in the phone...

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
player1.name='!!!'
player1.speak='BOOOOOOO'
print(player1.speak)
# this is BAAAAAAADDDDD 'because anything can happen to code like any programmer can come and make changes according to them...they can change your whole code without you even knowing about it as it is also accessbile to them(programmers)
# And now all that hard work that we put into our class has been overridden by this.
# We will have our run and speak, but player one now is completely useless.
#Completely useless.


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# HOW TO PROTECT HIDDEN CODE FROM BEING MODIFIED...
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Now in Python, there's this idea of public and private, and this is related to our discussion of abstraction.
# The idea behind abstraction is that we hide away information and only give access to things that a user is concerned about...
# So ideally, we shouldn't have access to init.
# Ideally, we shouldn't be able to, let's say modify, run or modify name and h, because when we create a player character in our game, hopefully the player can just randomly change their name or their age.
# So can we make a private variable in our class?
# Some languages allow us to have private variables, for example, in a language like Java.
# But in Python, there's no true privacy, no true private variables.
# Well, what we would do is do underscore name or underscore H.
# Does this give any special power?
# No, this is just a convention that is as programmers, as Python programmers, we determined that,
# hey, if we see underscore in our code, that most likely means that this should be a private variable.
# let keep it private--So if you ever want to keep a method or a an attribute private, you just put an underscore in front guarantee
# Dunder methods also works in same way like if there are two underscores in a function we are shoult not be modifying it...
# So this idea of a private field is important to Python.
# And although we can overwrite a lot of things, it's bad practice.
# The idea is to abstract away this code, and although it can be modified and overridden by using these proper conventions like private attributes, we're able to abstract things away, but still make sure that whatever the user might be using isn't going to break our code.





