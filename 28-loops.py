#loops
#allows us to run lines of codes over and over again

#item is variable we created
#zero to mastery is iterable that can be iterated over
#iterable cam be list,dict,tuple,set,string
#iterated->one by one check each item in the collection.
for item in 'zero to mastery':
    print(item)
    
for item in (1,2,3,4,5):
    print(item)

for items in (1,2,3,4,5):
    for x in ['a','b','c']:
        print(items,x)

