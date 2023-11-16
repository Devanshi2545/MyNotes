print('a'>'A')
#The output for `print('a' > 'A')` in Python would be `True`. 

#This is because, in the ASCII character set, the lowercase letter 'a' has a higher numerical value than the uppercase letter 'A'. When you compare these two strings using the greater-than (`>`) operator, it compares their ASCII values character by character, and since the ASCII value of 'a' is greater than that of 'A', the result is `True`.
print(1<2<3<4)
print(1<2>3<4)#here code will short circuit at 2>3 and return result as false...

#less than equal to
print(1<=0)

#not equal to
print(1!=0)

#equal to
print(1==2)

#logical operators <,>,==,>=,<= ,!= ,not(keyword but also a function)

print(not(True))

