# *args **kwargs
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