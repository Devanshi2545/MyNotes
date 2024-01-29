#List Comprehension
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

#Example:

#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

#Without list comprehension you will have to write a for statement with a conditional test inside:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)





mystring='hello'
mylist=[]

for letter in mystring:
    mylist.append(letter)
print(mylist)

#optimized way o doing this

mylist=[letter for letter in mystring]
#letter(any variable to iterater) for loop letter(iterable variable(should be same as before the for loop)) in mystring(object that we have to iterate)...
print(mylist)

mynum=[num for num in range(0,11)]
print(mynum)

numsquare=[num**2 for num in range(0,5)]
print(numsquare)

#even no
mylist=[x for x in range(0,11) if x%2==0]
print(mylist)

#celcius to farhenhiet
celcius=[0,10,20,34.5]
fahrenheit=[((9/5)*temp+32) for temp in celcius]
print(fahrenheit)

#even or odd using if and else loop
results=[x if x%2==0 else 'odd' for x in range(0,11)]
print(results)
#nested loop
mylist=[]
for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist.append(x*y)
        
print(mylist)
#optimized way
mylist=[x*y for x in [2,4,6] for y in [1,10,1000]]
print(mylist)