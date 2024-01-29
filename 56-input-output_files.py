#%% writefile myfile.txt
#hello this is a text file
#this is the second line 
#this is the third line 

#To open the file 
myfile=open('myfile.txt')

#To know present working directory or location just type
pwd

myfile.read()
#this will present all the content in text file and \n means new line starts 
#read() : Returns the read bytes in form of a string. Reads n bytes, if no n specified, reads the entire file.
#agr hm baar baar read file krenge run one after the other on the second run it wont show anything as a cursor works on it jb hm read krte hain file then vo cursor line ke end mein aa jata hain and so to read it again we need to reset it so it is done by using seek() function and so we use
myfile.seek(0)
#The seek() method sets the current file position in a file stream.

#The seek() method also returns the new postion.
#Syntax
#file.seek(offset)
#Parameter Values
#offset	Required. A number representing the position to set the current file stream position.
myfile.read() #now it will print the text in the file

myfile.readlines()
#each line will be shown seperate object to work with
#now we can loop through the object

