#STRINGS-a piece of text
#written in single or double colons
#type=str
username='supercoder'
password="supersecret"
#Another way of printing string is be using 3 single colons
#for long strings...we can do multi lines with three single qoutes....mostly used for long paraghs
long_string='''
wow
0  0
---
'''
print(long_string)


first_name='Devanshi'
last_name='Rana'
f_name=first_name+last_name
print(f_name)
full_name=first_name+' '+last_name
print(full_name)
#-----------------------------------------------------------------
#String concatenation-adding strings together
#String concatenation only works with strings
print('Devanshi'+'Rana')
#print('Devanshi'+5)#error
#-----------------------------------------------------------
#TYPE CONVERSION
print(str(100))
print(type(str(100)))
#Here we converted 100 into string by using predefined functions 'str'
print(type(int(str(100))))
#converted str type 100 back to int
