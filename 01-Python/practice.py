#return true if any number is even inside a list
def check_even_list(num_list):
    even_number=[]
    for number in num_list:
        if number%2==0:
            even_number.append(number)
            
        else:
            pass
    return even_number
        
print(check_even_list([1,2,3,4,5]))

#we didnt use false in else statement because in cases where we had odd at first place then it will return false
# our motive is to check whether there is any even number in the list or not


#------------------------------------------------------------
#WAP that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def lesser_of_two(a,b):
    if a%2==0 and b%2==0:
        if a<b:
            result=a
        else:
            result=b
    else:
        if a>b:
            result=a
        else:
            result=b
            
    return result


#optimized way
def lesser_number(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)
    
    
result=lesser_number(7,5)
print(result)


#write a function takes a two-word string and return True if both words begin with same letter
def animal_cracker(text):
    wordlist=text.lower().split()
    return wordlist[0][0]==wordlist[1][0]
#if wwe dont use upper case or lower case then same letter if capital or small give false as outpue
#say Crazy cat give false as for capital or small 'c'
result=animal_cracker('Levelheaded Llama')
print(result)
result1=animal_cracker('Crazy cat')
print(result1)


#Given two integers, return True if the sum of the integers is 20 or it one of the integer is 20.If not , return False
def makes_twenty(n1,n2):
       return n1+n2==20 or n1==20 or n2==20
   
result=makes_twenty(10,20)
print(result)
       
#----------------------------------------
#given a string , return a string where for every character in the orginal there are three characters

def paper_doll(text):
    result=''
    for char in text:
        result+=char*3
    return result
        
print(paper_doll('hello'))
        

    
