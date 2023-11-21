#parameter-->variables assigned in bracket of any defining funtion...

#parameter->used when we define the functions...
def say_hello(name,emoji):
    print(f'hellllooooooo {name} {emoji}')
    
#arguments-used when  we call the functions...or evoke the functions...
say_hello('Devanshi','><')#these are postional arguments
say_hello('Chirag','()')
say_hello('peter','00')

# A PARAMETER is the variable listed inside the parentheses in the function definition.
# An ARGUMENT is the value that are sent to the function when it is called.
#---------------------------------------------------------------------------------------------------
#POSITIONAL ARGUMENTS
# Arguments we mentioned above are pos. arg. as there postion matters...
# required to be in a proper position...

#  KEYWORD ARGUMENTS
# Doesnt need proper position
say_hello(emoji='00',name='bibi')
say_hello(name='bibi',emoji='00')
#Both have different positions but are giving same output so here proper order doesnt matter...
# Not to be used bcz it makes code more confusing...
#they are sometimes confused with DEFAULT PARAMETERS...



# DEFAULT PARAMETERS-par. allow us to give what we want default...
#It is used for incase you forgot to give arguments then there on calling the function default parameter will be printed...
#they are written in paranthesis of a funtion while defining it...
def say_hello(name='DEVIL',emoji='<.>'):
    print(f'hellllooooooo {name} {emoji}')
say_hello('Devanshi','><')
say_hello('Chirag','()')
say_hello('peter','00')
say_hello()# no arguments given so here default parameters will be printed
say_hello('timmy') #here we have not given second parameter so it will pick up second default parameter of its own...




 
