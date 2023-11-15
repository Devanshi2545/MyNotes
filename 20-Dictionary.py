#Dictionary
#datatype in python and also a data structure
#it has a key (string) and a value
#Dictionary is an unordered key-value pair
#value could be anything ie-list,array,string,char,int,boolean...

dictionary={
    'a':1,
    'b':2,
    'x':3
    
}
print(dictionary)


example={
    'a':[1,2,3],
    'b':'hello',
    'x':True
}
    #dictionary format

my_list=[{'a':[4,5,6],
          'b':'hello',
          'c':True}]
#dictionary in list format so we must need starting index too...

print(my_list[0]['a'][2])
print(example['a'][1])

#WHEN TO USE A LIST AND WHEN TO USE A DICTIONARY
#Dictionary is unsorted and has no order
#list has order as it has indexes 
#ex-if you have people in line and you want their names orv erwise may be you should use lists...
#may b e you have a user that is playing a game and has kept a usrname that doesnot need to be in any order to store their you can use dictionary
#dictionay holds a lot more information than list as list contains index and value
#dictionay value can hold upto any sort of datatype

#dictionay keys need to have a special property
dictionary={
    123: [1,2,3],
    True:'hello',
    'cc': True
    #[100]:False  (will show error)
    
    #string is immutable but a list is mutable so becuase of thay keys should be stored in a location that is not changed 
    #dictionary doent want its va            lue to be changed...
    #dictionary key always imutable...
    #dic key has to be unique that is exist only once...
}
print(dictionary[123])

user={
    'basket':[1,2,3],
    'greet':'hello'
}
print(user.get('age'))
#if something we are searching is not in the dict it will show an error and will not compile after that...
#in order to avoid errors we will use .get method...it will search for the value entered and tell the answer...it the value is not present it will show none
#and the code will compile furthermore...
#say if we dont have age in our dictionary aur agr age nhi hai to hme ek default value chahiye then hm , daalke default value bhi likh skte hain...
#incase age doesnt exist we get a default value...
#but if it exist then we will get age value and not the default value...

print(user.get('age',55))

# ANOTHER WAY TO FORM A DICTIONARY

#user2=dict(key=value)
user2=dict(name='Devanshi')
print(user2)


user={
    'basket':[1,2,3],
    'greet':'hello',
    'age':20
}
print('basket' in user)
print('size' in user)
#finding keys and values in dict
print('age' in user.keys())#.keys check whether the word before in is there in keys side of dictionary...
print('hello' in user.values())#.values() check whether the word before in is there in value side of dictionary...

print(user.items())#grabs entire items of dict...every key value pair is actually a tuple ex- 'basket':[1,2,3] is tuple1,,,, 'greet':'hello' is tuple 2,'age':20 is tuple3

#clear dict
print(user.clear)#creates an empty dict...

#copy dict
user2=user.copy()#copy contents to new variable
print(user.clear())
print(user2)

#pop-poping key 
user3={
    'basket':[1,2,3],
    'greet':'hello',
    'age':20
}
print(user3.pop('age'))#pops the key in the bracket and returns its value as an output...
print(user3)

#popitem
print(user3.popitem())#removes the last key:value pair that was inserted into the dictionary...
print(user3)

#update
print(user3.update({'age':55}))
print(user3)
#if key is not present n the dictonary it will automatically add that tuple to the dictionary...




