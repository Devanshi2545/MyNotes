#SET-unordered collection of unique objects
#unlike dict we dont have key:valus but just values
#there are no duplicates
#all are unique and so are on one location in memory
#set object doesb=no support indexing
#print(my_sets[0])->output error
my_sets={1,2,3,4,5}
my_sets.add(100)
my_sets.add(2)
print(my_sets)
#here 100 is add to the set because prev set doesnot contain 100...it is unique object so it added to set but 2 is not added again because it already occured in the set...

my_list=[1,2,3,4,5,5]
print(set(my_list))

my_sets={1,2,3,4,5,5}
print( 5 in my_sets)
print(len(my_sets))
print(list(my_sets))#because in set 1st occurance of 5 will be counted as it is unique 2nd 5 will not be counted (not unique)
new_set=my_sets.copy()
print(new_set)

#METHODS IN SETS-->these will modify our set but dont return any value
my_set={1,2,3,4,5}

your_set={4,5,6,7,8,9,10}

#1 .difference()
print(my_set.difference(your_set))#my_set mein jo different hai vo output dega 
#jo different your_set mein hai vo nhi because hmse difference my_set ka nikala hai your_set se
#.difference ke age jo bhi set hoga uski different values print hongi...


#2 .discard()

print(my_set.discard(5))#discarding 5 from my_set
print(my_set)

#3 .difference_update()
my_set.difference_update(your_set)#remove all elements of another set(your_set) from this set(my_set)...
print(my_set)

#4 .intersection
my_set={1,2,3,4,5}

your_set={4,5,6,7,8,9,10}
print(my_set.intersection(your_set))#prints common values from both the sets...
print(my_set & your_set)

#5 .isdisjoint
#disjoint means these sets have nothing i common
#if nothing is common then it will return true...if some objects are common it will return true...

print(my_set.isdisjoint(your_set))


#6 .union
print(my_set.union(your_set))#print all unique elements of both sets in first set
#can also be written as
print(my_set | your_set)

#7 .issubset
my_set={4,5}

your_set={4,5,6,7,8,9,10}
print(my_set.issubset(your_set))
#when all element of this set(my_set) are also in other set(your_set) then it returns true value else false(when all elements of this set are not in other set)...
#returns whether other set contains this set or not


#8 .issuperset
print(my_set.issuperset(your_set))#return false when this set doesnt contain all elements of other set...
#return true when this set contains all elements of other set...

print(your_set.issuperset(my_set))#here your_set contains all elements of my_set
#returns whether this set contains other set or not













