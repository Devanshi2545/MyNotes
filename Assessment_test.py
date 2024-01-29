#Assessment test(bootcamp course)(Lecture 40)
st='Sam Print only the world that start with s in the sentence'
for word in st.split():
    if word[0].lower()=='s':
        print(word) 
#use range() to print all even numbers 0,10    
mylist=list(range(0,11,2)) 
print(mylist)    
  
  
st='Print every word in this sentence that has an even number of letters'
for word in st.split(): 
    if len(word)%2==0:
        print(word  +  'is even.')
        
st='Create a list of the first letters of every word in this string'
list1=[word[0] for word in st.split()]
print(list1)