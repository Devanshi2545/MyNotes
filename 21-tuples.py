#tuples-immutable lists that cannot be modified
#can run reverse on tuple
#example-we can create a new tuple everytime a user requests a new pickup location
#tuple is a completely valid key in python 
my_tuple=(1,2,3,4,5)
print(my_tuple[2])
print(5 in my_tuple)

user={
    (1,2):[1,2,3],#tuple1
    'greet':'hello'#tuple2
}
print(user.items())
print(user[(1,2)])# tuples can also be returned in a dictionary

new_tuple=my_tuple[1:2]
print(new_tuple)
#whenever we have single value in a tuple tends to have a  ',' after it...
x,y,z,*other=(1,2,3,4,5)#tuples can also be written in short form i  this way...
print(x)
print(y)
print(other)
print(z)

#PYTHON TUPLE METHODS
#1. count()
#2. index()
my_tuple=(1,2,3,4,5)
print(my_tuple.index(5))#will give answer of the value that is in bracket of index...

print(my_tuple.count(4))#will count number of occuances of the value inside count bracket...

print(len(my_tuple))