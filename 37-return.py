# function hastwo types ie. with return-return something or with return -just modifying
# when compilers run over return function it says whaterver runs after the function ends is returned 

def sum(num1,num2):
    print('hiii')
    return num1 + num2
#should do one thing really why
#should return something
print(sum(10,5))
    

def sum(num1,num2):
    
    return num1 + num2
total=sum(10,5)
print(sum(10,total))#10+15
#or can be written as
print(sum(10,sum(10,5)))
#------------------------------------------------------------------------------------------------------------------
# we can define function in a function
def sum(num1,num2):
    def another_func(n1,n2):
        return n1+n2
    return another_func(num1,num2)
    return 5#wont return these two functions because as soon as return functions returns a function it exist a function...
    print('hello')
    
total=sum(10,20)
print(total)
    
    