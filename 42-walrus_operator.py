 # := assigns value to variable as a part of a larger expression...
 # in if or while statement
 
a='helllooooooooo'
if(len(a)>10):
    print(f"too long {len(a)} elements")
    
# using walrus operator
if((n:=len(a))>10):
    print(f"too long {n} elements")
    
    
while((n:=len(a))>1):
    print(n)
    a=a[:-1]
