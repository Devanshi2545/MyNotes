#while loops-while condition:
# With the while loop we can execute a set of statements as long as a condition is true
i=0#indexing variable...in while loop it is a must to define value of indexing variable
while i < 50:
    print(i)
    i=i+1#make sure to inc/dec else loop will run in infinite loop...
    
else:
  print('done with all the work')
  
  #WHEN TO USE WILE LOOP OR FOR LOOP
  my_list=[1,2,3]
  for item in my_list:
      print(item)
      
i=0
while i<len(my_list):
    print(my_list[i])
    i+=1
    break

#most useful way to use while loop 
#while loops are useful for task for looping where you dont know that how many times you have to run the loop until the condition is no more TRUE...
while True:
    response = input('say something: ')
    if(response=='bye') :
        break
    
#when we use a BREAK statement we break out of the loop that is exit it...
#when we use CONTINUE it goes back to the for or while loop...
my_list=[1,2,3]
for item in my_list:
    continue
    #print(item)
#now on line 33 where continue is executed it will dont go furthermore but go back to the for loop line 32...it will not go to the print statement

#PASS-doent do anything but passes to next line 
#used as place holders when you dont know what could be done so meanwhile you pass for the loop or something
my_list=[1,2,3]
for item in my_list:
#thinking about it
   pass
i=0
while i<len(my_list):
    print(my_list[i])
    i+=1
    pass

