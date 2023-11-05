#ESCAPE SEQUENCE
#What if we wanted to have a string that tells me, let's say, the weather and here we want to write.

#It's sunny.

#You see how the highlighting changed here?
#----------------------------------------------
#weather='it's sunny'




#Because I want to say it's with an apostrophe s, but.


#Python is reading this and saying, okay, this is the start of the string and this is the end of the string.

#And then I have no idea what this is.

#And then we're starting a string again.

#How can we fix this?

#Well, we can add a double quote string instead.

#And this now works.
weather="it's sunny"

#But what if for some reason we also wanted to add its.

#Kind of sunny in quotation marks.

#Well, now we have another issue.

#So how can we solve this?

#Because in human language, we have double quotes and apostrophes.

#Well, we can use escape sequences here.
#---------------------------------------------
#weather="it's"kind of"sunny"


#And this is a little hard to understand at first, but it's simply adding a splash like this.

#So the one right above your enter on the keyboard.

#So this slash, when Python goes through, it is going to say, all right, whatever comes after this,

#I recognize this symbol.
#----------------------------------------------------------
weather="it\'s \"kind of\"sunny"

#Whatever comes after this, I'm going to assume it's a string.

#So now if I do backslash here and then backslash here, it's going to say, hey.
# I'm letting you know what comes after.

#This is a string.


#So that when we print the weather.





#Now this escape sequence can be used in multiple ways.

#For example, if I want to have an actual backslash, well, I can go like this.


#And because it's saying whatever comes after this is a string, it's going to assume that this is a string now.

#So if I run this, you see that we get this backslash and there's a few other neat tricks that you can

#do with it.


#For example, one of it is the backslash t.
weather="\tIt\'s\"kind of\"sunny \n hope you have a good day!"

#What does that mean?

#Well, let's remove this for now.


#There you go.


#The backslash t remember, let's add a space in here so we can distinguish.


#It is going to say, Hey, whatever comes after this, I want you to add a tab.

#This is a special meaning here.


#So if I click on Run.

#You see that?

#It's added a tab spacing to my string.

#Another one is using N or a new line.


#So let's leave T here and then add a backslash n and then say.


#Hope you have a good day.


#What do you think will happen here if I click Run?

#I have a tab.

#From the backslash.


 #And then I have a new line after kind of sunny because I do the backslash and which denotes a new

#line so that this shows up on a new line.
print(weather)


#Now, these escape sequences are hard to see at first, but they're pretty much available in all programming languages.

#They use strings.


#So if you come from another language, this shouldn't be that strange to you.


#If it's your first time seeing this, you just need to get used to this syntax and every once in a while

#go to the Python documentation and just type in escape sequences and you'll see all the ones that we have.

#These are the main ones that you need to know.
