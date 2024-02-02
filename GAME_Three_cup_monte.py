example=[1,2,3,4,5,6,7]
from random import shuffle
shuffle(example)#doesnt return anything but just shuffles the string

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
result=shuffle_list(example)

print(result)

mylist=['','o','']
shuffled=shuffle_list(mylist)
print(shuffled)

def player_guess():
    guess=''
    while guess not in ['0','1','2']:
          guess=input("Pick a number:0,1,2")
    
    return int(guess)

my_index=player_guess()

print(my_index)

def check(mylist,guess):
    if mylist[guess]=='O':
        print("correct")
        
    else:
        print("wrong")
        print(mylist)
        
        
mylist=['','O','']
mixeduplist=shuffle_list(mylist)
guess=player_guess()
check(mixeduplist,guess)
    
    
    
    
