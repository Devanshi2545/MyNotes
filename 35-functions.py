# DRY used...functions are really useful when a task is to be repeated again and again
# when program is to be run for multiple times...
# 
# def->define 
def say_hello():
    print('helloooo')
say_hello()

picture=[
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0] 
]
def show_tree():
    for image in picture:
     for pixel in image:
        if(pixel==1):
            print('*',end='')
        else:
            print(' ',end='')
     print('')
    
show_tree()
show_tree()
show_tree()


# Join all items in a tuple into a string, using a hash character as separator:
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

#The join() method takes all items in an iterable and joins them into one string.

#A string must be specified as the separator.
#Join all items in a dictionary into a string, using the word "TEST" as separator:
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)
