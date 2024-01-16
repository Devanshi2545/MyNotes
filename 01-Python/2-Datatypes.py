#Fundamental Data type-values in python
#integers-int-3
#floating point-float-3.09
#strings-str-" "
#lists-list-[ ]
#dictionary-dict-{Unordered key:value pairs}
#tuples-tup-( )
#sets-set-{ }
#booleans-bool-true or false
int #integers
#3 4 5 ...are  numbers.Integer is used for numeric calculations
print(2+4)
print(2-4)
print(2*4)
print(2/4)
#check type 
print(type(2+4))
#it will print class 'int'
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
float
#floating point number is simply a number with decimal point
#example 0.5,7.09 etc...
print(type(0.001))
print(type(33+1.1))
print(type(11.0))
#here class type will be float
#DIFFERENCE BETWEEN FLOAT AND INT
#We know these numbers are to be stored n memory in binary form and floating numbers take more space and is difficult to represent in binary form so for binary it has to store number in two different locations 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#EXPONENT POWER-->number**number(power)
print(2**2)
#it will print 2's power 2 ie 4
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#DOUBLE DIVIDE CONCEPT-class type int.It rounds off the value
#single divide mein class type is float
print(2//4)
print(4//4)
print(7//2)#3
print(7/2)#3.5
print(type(8//2))
print(type(7/2))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#MODULUS(%)
#It tells the remainder
print(5%4)
print(6%4)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#math functions
#----------------------------------
#round() Round a number to a given precision in decimal digits.
print(round(3.9))
#-----------------------------------
#abs()-gives absolute vlaue ie no negative number
print(abs(-20.1))
bool
str
list
tuple
set
dict
#these work for storing and modifying information
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#classes
#beyond these defined data types we can create custom types of our own called classes
#ex-supercars
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#specialized datatypes
#They're not built into Python, but they're special packages and modules that we can use from libraries.

#Now, again, this is a topic that we'll cover later, but these are you can think of it as extra boosts

#whenever we don't have a data type that we want in the standard Python package.

#And maybe we don't want to create our own custom types.

#There are specialized data types that we can use from what we call modules.

#So you can think of it as extensions that we can add to the language.


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
None
#As the name suggests, means nothing.
#It's kind of like the idea of zero in math.
#It's the absence of value.
#---------------------------------------------------------------------
# PYTHON uses dynamic typing...
# PROS AND CONS OF DYNAMIC TYPING
#PROS
#1. very easy to work with
#2. faster development time
#CONS
#1. may result in bugs for unexpected datatypes!
#2. you need to be aware of type()