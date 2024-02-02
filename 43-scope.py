#scope-what variables do I have access to?
# A variable is only available from inside the region it is created. This is called scope.
# A variable created inside a function is available inside that function:
def myfunc():
    x=300
    print(x)
    
myfunc()

# As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function

# FUNCTION INSIDE A FUNCTION
#As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#GLOBAL SCOPE
#A variable created in the main body of the Python code is a global variable and belongs to the global scope.

#Global variables are available from within any scope, global and local.
#A variable created outside of a function is global and can be used by anyone
x = 300

def myfunc():
  print(x)

myfunc()

print(x)
#----------------------------------------------------------------------------------------------------------------------
#SCOPE RULES
a=1

def confusion():
    #local scope(that is inside the function)
    a=5
    return a
print(a)
print(confusion())

#1-start with local
#2-parent local?(first functioncheck krenge agr hmare paas nest function hai)
#3-Global
#4-built in python functions.
#-------------------------------------------------------------------------------------------------------------------------
#GLOBAL KEYWORD
a=10
def confusion(b):
    print(b)
    a=90
confusion(300)
#---------------------------------------------------
#total =0
#def count():
 #   total+=1
 #   return total
#count()
#here error will pop because total is not declared in the function and no matter how many times you call the function its not gonna print it
#so we will use global keyword before totalso instead of creating a new variable we can use the same variable in and out of the function...
total=0
def count():
    global total 
    total += 1
    return total
count()
count()
print(count())
#but this becomes difficutl in future when we have long codes and so many variables to assign 
#what we can do is:
total=0
def count(total):
    total+=1
    return total
print(count(count(count(total))))
#this is insane to write like this

#-----------------------------------------------------
#non local-variables that are not global locals but csn be used in other function using the word -->non local before that vsriable
def outer():
    x='local'
    def inner():
        nonlocal x
        x='nonlocal'
        print("inner:",x)
    inner()
    print("outer:",x)
outer()
#---------------------------------------------------------------

# why do we need scope?
#machines dont have inifinite power,dont have infinite power,memory,CPU
#so it can lead to crashing of power,CPU
#we use scope as is we have a variable whose memory is stored at some place so to use the variable from one memory location we use scope
#once the function value is returned everything in function goes into a garbage value...


#SCOPE follows LEGB Rules
#L:= LOCAL
#E:=ENCLOSING FUNCTION LOCALS(def or lambda)
#G:=GLOBAL(module)
#B:=BUILT-IN(python)

#LEGB stands for Local, Enclosing, Global, and Built-in, which represents the four scopes in Python where a variable can be defined and searched for. These scopes form the basis of Python's variable resolution mechanism.

#1. **Local (L)**: Variables defined within a function are in the local scope. They are accessible only within that function.


def example_function():
        local_variable = 10
        print(local_variable)

example_function()  # Output: 10
    # Uncommenting the line below would result in an error since local_variable is not defined outside the function.
    # print(local_variable)

#2. **Enclosing (E)**: This scope is relevant when we have nested functions. It refers to the enclosing function's scope.


def outer_function():
        outer_variable = 20

        def inner_function():
            print(outer_variable)

        inner_function()

outer_function()  # Output: 20


#3. **Global (G)**: Variables defined at the top level of a script or module are in the global scope. They are accessible throughout the entire module.


global_variable = 30

def example_function():
        print(global_variable)

example_function()  # Output: 30
    

#4. **Built-in (B)**: This is the widest scope and includes names like `print()`, `len()`, etc., which are built-in functions in Python.

    
print(len([1, 2, 3]))  # Output: 3
    

#When a variable is referenced, Python searches for it in the following order: Local, Enclosing, Global, and Built-in. If the variable is not found in any of these scopes, a `NameError` is raised.

#Here's an example that demonstrates the LEGB concept:


global_variable = "I am global"

def outer_function():
    outer_variable = "I am enclosing"

    def inner_function():
        inner_variable = "I am local"
        print(inner_variable, outer_variable, global_variable)

    inner_function()

outer_function()
# Output: I am local I am enclosing I am global


#In this example, `inner_function` can access variables from its local scope (`inner_variable`), its enclosing scope (`outer_variable`), and the global scope (`global_variable`).

#Above global is only the built in level
x=50
def func(x):
    print(f'X is {x}')
    x=200
    print(f'I just locally change x to {x}')
    
print(func(x))
print(x)

#what is you want to reassign global x(x=50) to local x(x=200) as we know local xx in not going to work outside the function
# so for that we need to declare 'global' keyword in the function 
#uske assign krdenge in the function by using keyword 'global'
x=50

def func1():
    global x
    print(f'X is {x}')
    #local reassignment on a global variable!
    x='NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')
    
print(func1())
print(x)


#--------------------------------------------------------
#instead of using global varibale unless much needed
#what we can do is:
def func2(x):  #pass x as an argument
    print(f'X is {x}')
    #REASSIGN the local variable
    x='NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')
    return x
#print(x)
x=func2(x)
print(x)
#the ouput is same as that of global keyword but is much cleaner and safer than the code above(with global keyword) bcz its quite dangerours to have a reassignment take place of the kyword. we may accidently rewrite or overlap the variable value that makes it harder to debug the program





 



      
      
