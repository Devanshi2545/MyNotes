print(True==1) #(true==bool(1)) so true
print(''==1)#(''(false)==1(bool(1))) so false
print([]==1)
print(10==10.0)
print('1'==1)#false because of type conversion bacause(char==int)

#== checks for equality of value...

# is checks if the location in memory where value is store is same or not...
print([1,2,3] is [1,2,3]) #false
#everytime a data structure is created it is created in a different memory space hether their values are same...
print('1' is '1')#true
print(10 is 10.0)#false
print([] is [])#false
#these are two list with completely different memory locations


