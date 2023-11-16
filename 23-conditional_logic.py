is_old=False
is_licensed=True

if is_old:
    print('you are old enough to drive.')
print('checkcheck')
#The if statement evaluates condition.
#If condition is evaluated to True, the code inside the body of if is executed.
#If condition is evaluated to False, the code inside the body of if is skipped.


#if-else

#An if statement can have an optional else clause.

#The syntax of if...else statement is:
#-------------------------------------------  
#if condition:
    # block of code if condition is True

#else:
    # block of code if condition is False
#-------------------------------------------- 
#The if...else statement evaluates the given condition:

#If the condition evaluates to True,

#the code inside if is executed
#the code inside else is skipped
#If the condition evaluates to False,

#the code inside else is executed
#the code inside if is skipped 
#example
number = 10

if number > 0:
    print('Positive number')

else:
    print('Negative number')

print('This statement is always executed')


#if...elif...else
#The if...else statement is used to execute a block of code among two alternatives.

#However, if we need to make a choice between more than two alternatives, then we use the if...elif...else statement.

#The syntax of the if...elif...else statement is:
#----------------------------------------------------------------------
#if condition1:
    # code block 1

#elif condition2:
    # code block 2

#else: 
    # code block 3
#-----------------------------------------------------------------------
#If condition1 evaluates to true, code block 1 is executed.
#If condition1 evaluates to false, then condition2 is evaluated.
#If condition2 is true, code block 2 is executed.
#If condition2 is false, code block 3 is executed.

#there can be more tham elif conditions...
#example
number = 0

if number > 0:
    print("Positive number")

elif number == 0:
    print('Zero')
else:
    print('Negative number')

print('This statement is always executed')

#Python Nested if statement
#We can also use an if statement inside of an if statement. This is known as a nested if statement.

#The syntax of nested if statement is:
#----------------------------------------------------------------------------------
# outer if statement
#if condition1:
    # statement(s)

    # inner if statement
   # if condition2: 
        # statement(s)
#-----------------------------------------------------------------------------------
#Notes:

#We can add else and elif statements to the inner if statement as required.
#We can also insert inner if statement inside the outer else or elif statements(if they exist)
#We can nest multiple layers of if statements.
number = 5

# outer if statement
if (number >= 0):
    # inner if statement
    if number == 0:
      print('Number is 0')
    
    # inner else statement
    else:
        print('Number is positive')

# outer else statement
else:
    print('Number is negative')

# Output: Number is positive

#also if statement can be written using operators\
is_old=False
is_licensed=False

if is_old and is_licensed:
    print('you are old enough to drive and you have a license!')
else:
    print('you are not of age!')
print('okoko')

#--------------------------------------------------------------------------------------------------------------------------------------------
#truthy and falsy value
print(bool('hello'))#output=true so truthy value 
print(bool(5))#output=true so truthy value 
print(bool(0))#output=false so falsy value
print(bool(' '))#output=false so falsy value
#values considered as falsy
#none
#false
#0
#0.0
#0j
#decimal(0)
#fraction(0,1)
#[]
#{}
#()
#''
#b''
#set() and many more
#an emplty range say for i in range(0)
#object for which 
#obj.__bool__() returns false
#obj.__bool__() returns 0

password='123'
username='johny'

if password and username:
    print('you are old to drive and you have a license')
else:
    print('you are not of age!')
    
print('okokok')
#-------------------------------------------------------------------------------------
#Ternany operators-conditional expressions
#shortcut for if-else loop in certain conditions

#condition_if_true if condtion else condition_if_false
is_friend = True
can_message="message allowed" if is_friend else "not allowed to message"
print(can_message)#obj.__bool__() returns false

