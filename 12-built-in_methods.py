#example of some built in functions
#str()
#int()
#round()
#len()
greet='hellooooooo'
print(greet)
print(greet[:])
print(len(greet))
print(greet[0:len(greet)])#will print the whole word

#built in methods usually contain a dot(.) in fronth of them
#example
# format()-it formats strings
#Go to python string methods on google to know more...
#some built in methods 
qoute='to be or not to be'
print(qoute.upper())
print(qoute.capitalize()) #first word of the sentence capital
print(qoute.find('b'))# if the letter in their in the string then it will tell the first position of the letter
print(qoute.replace('be','me'))
print(qoute)#here original value of qoute will be printed as we know strings are immutable ie. they cannot be changed ,,,we can create them or destroy them
qoute2=qoute.replace('be','me')
print(qoute2)#here we created a new string from an old string but we have not modified the original string in their variable...

#https://docs.python.org/3/library/functions.html to know more about built in methods