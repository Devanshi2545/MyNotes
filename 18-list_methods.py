basket = [1,2,3,4,5]
print(len(basket))
#We have some list methods that we can use to modify the list... we simply need to put a dot(.) and write method in it...

#adding ----> append
new_list=basket.append(100)
#print(basket)
# here basket was appended with a new number 100 at the end of the list
# but if we tried to store it in a new variable it will show none because append changes list in place ....it doesnt produca any value
# it dosent create a new list but just adding an element to the list...
 
 #inserting
new_list=basket.insert(5,100)
 #insert(position,value)
 
 #extend
new_list=basket.extend([100,101])
##will exten the list further more 
#print(new_list)


#REMOVING
basket.pop()
basket.pop(0)
print(basket)
# pop- we put index we want to remove

#remove-we put value we want to remove
 
new_list=basket.remove(100)
print(new_list)
print(basket)
 
# all these methods doesnot return a value but changes the original array(jis array ke baad hmne dot lgaya hai!!!)
# so if we add these to a new variable it will show 'none' as the output
#we get none because it is not producing or returning anything...

#clear-->clears everything in the list...
new_list=basket.clear()
print(new_list)
print(basket)

#index
basket=['a','b','c','d','e']
print(basket.index('b'))
#index tells index of the value provided in the bracket...
#we can also give a range to find index of a value
#index(value,start,stop)
print(basket.index('b',0,3))


#keywords in python-words means something like and ,or ,in etc
print('b' in basket)

# count- tells how many times the value occured
print(basket.count('d'))

#sorting
basket.sort()
print(basket)
#difference between . sort()(method) and sorted(value) (function)
#.sort( ) will sort values in original list and doesnt return value so it we assign it to a new variable it will show output as none
#sorted(value) will itself create a new sorted list... it will return some value so it we assign it to a new variable it will show us the sorted list...

new_basket = sorted(basket)
print (new_basket)


new_basket= basket[:]# copying content of basket in new basket variable
#we can use method called copy() to copy content to a new variable

new_basket= basket.copy()
new_basket.sort()
print(new_basket)

#reverse
basket.reverse()
print(basket)

print(basket[::-1])

print(range(1,100))
print(list(range(1,100)))
print(list(range(101)))

#JOIN
sentence=' '
new_sentence=sentence.join(['hi','my','name','is','jojo'])
print(new_sentence)


new_sentence=' '.join(['hi','my','name','is','jojo'])
print(new_sentence)


#LIST UNPACKING
a,b,c=[1,2,3]
print(a)
print(b)
print(c)

a,b,c,*other,d,e=[1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)
print(e)



