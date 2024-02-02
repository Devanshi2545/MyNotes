# *args ,**kwargs
# The special syntax *args in function definitions in Python is used to pass a variable number of arguments to a function. It is used to pass a non-keyworded, variable-length argument list...
def super_func(*args):
    print(args)
    return sum (args)
print(super_func(1,2,3,4,5))
# The special syntax **kwargs in function definitions in Python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is that the double star allows us to pass through keyword arguments (and any number of them).
def second_fun(*args,**kwargs):
    #print(kwargs)
    total=0
    for items in kwargs.values():
        total+=items
    return sum(args)+total
print(second_fun(1,2,3,4,5,num1=5,num2=10))

# RULE: params, *args, default parameters,**kwargs
def second_fun(name,*args,**kwargs):
    #print(kwargs)
    total=0
    for items in kwargs.values():
        total+=items
    return sum(args)+total
print(second_fun('Devanshi',1,2,3,4,5,num1=5,num2=10)) 
#---------------------------------------------------------------------------------
def myfunc(a,b):
    return sum((a,b))*0.05
    
#so here a  and b are positional arguments 
#what if we want to assign more the two parameters
# we can do this we have to pass number of arguments
#say for ex we passed 5 arguments and we called 6 arguments inside the function so , it will show an error 
# to overcome this problem we use *argument
#
#In Python, *args and **kwargs are used in function definitions to handle variable numbers of arguments.

#*args (Arbitrary Arguments):

#*args return tuples
#** kwarg return dictionary

#It allows a function to accept any number of positional arguments.
#The *args syntax collects all the positional arguments into a tuple.
def example_function(*args):
    for arg in args:
        print(arg)

example_function(1, 2, 3)


#**kwargs (Arbitrary Keyword Arguments):

#It allows a function to accept any number of keyword arguments.
#The **kwargs syntax collects all the keyword arguments into a dictionary.
#Example:
def example_function(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

example_function(name="John", age=25, city="New York")

#Combining both in a function definition, you can use *args and **kwargs together:
def combined_example(*args, **kwargs):
    for arg in args:
        print(arg)

    for key, value in kwargs.items():
        print(key, ":", value)

combined_example(1, 2, 3, name="John", age=25)
# This allows the function to accept a variable number of both positional and keyword arguments.