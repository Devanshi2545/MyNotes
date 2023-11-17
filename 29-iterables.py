user={
    'name':'Devanshi',
    'age':21,
    'can_swim':False
}
for item in user:
    print(item)
    
for item in user.items():
    print(item)
    
#we can also write in another way
for item in user.items():
    key,value=item;
    print(item)
#or can be writte as:

for key,value in user.items():
    print(key,value)
    
#key,value are just variables and can be kept according to choice...
    

for item in user.values():
    print(item)
         
for item in user.keys():
    print(item)

#for item in 50:# cannot be iterable 
    #print(item)
