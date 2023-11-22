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







 



      
      
