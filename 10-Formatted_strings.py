#formatted string
#example you have to make an amazon user page
name = 'Devanshi'
age = 21
#print('hi ' + name +'. you are '+str(age) +' years old')
print(f'hi {name}. You are {age} years old.')
#The f before the string indicates that it's an f-string, allowing you to include variables and expressions inside curly braces.
#to make it dynamic we have to use 'f' word in starting of line and variables in curly brackets .
#remove all + signs and other signs...
#We can also write it in this way
print('hi {}.You are {} years old'.format('Johny','55'))
#keep in mind .format should come in print brackets...
#Whatever comes first fills in the first bracket...
#Another form of writing it is
print('hi {}.You are {} years old'.format(name,age))
#We can also write another name by making a new variable and calling them in bracket...
print('hi {new_name}. You are {age} years old'.format(new_name='Sally',age=100))
#we know counting starts from 0 ,1so if we give numbering in the brackets it would pick according to number sequence
print('hi {0}.You are {1} years old'.format(name,age))
