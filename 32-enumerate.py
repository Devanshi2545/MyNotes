#Often, when dealing with iterators,
# we also need to keep a count of iterations.
# Python eases the programmers’ task by providing a built-in function enumerate() for this task.
# The enumerate () method adds a counter to an iterable and returns it in the form of an enumerating object. 
# This enumerated object can then be used directly for loops or converted into a list of tuples using the list() function.

#Syntax: enumerate(iterable, start=0)

#Parameters:

#Iterable: any object that supports iteration
#Start: the index value from which the counter is to be started, by default it is 0
#Return: Returns an iterator with index and element pairs from the original iterableParameters:

#Here, we are using the enumerate() function with both a list and a string. Creating enumerate objects for each and displaying their return types. It also shows how to change the starting index for enumeration when applied to a string, resulting in index-element pairs for the list and string.
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print ("Return type:", type(obj1))
print (list(enumerate(l1)))

# changing start index to 2 from 0
print (list(enumerate(s1, 2)))
#----------------------------------------------------------------------------

l1 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly
for ele in enumerate(l1):
	print (ele)

# changing index and printing separately
for count, ele in enumerate(l1, 100):
	print (count, ele)

# getting desired output from tuple
for count, ele in enumerate(l1):
	print(count)
	print(ele)

#ENUMERATE can work on tuples,lists,arrays,strings
for i,char in enumerate((1,2,3)):
    print(i,char)
    
for i,char in enumerate([1,2,3]):
    print(i,char)
    
for i,char in enumerate('hellloooo'):
    print(i,char)
    
#--------------------------------------------------------------------
for i,char in enumerate(list(range(100))):
    print(i,char)
    if char==50:
        
     print(f'index of 50:{i}')