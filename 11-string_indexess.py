selfish= '01234567'
        #01234567
print(selfish[1])
#will print letter for mentioned index number
#default index starts from 0

#SYNTAX
#[start:stop:stepover]
#tells us sarting and ending index which we want to print
#stepover-tells us start here,end here and stepover few things 
print(selfish[0:4:1])#stepover one index
print(selfish[0:8:2])
print(selfish[1:])#start from 1 and go until string's last number...
print(selfish[:5])#print until index 5
print(selfish[::1])#print from 0 till string ends with stepover 1
print(selfish[::-1])#print string from backward ie reverse of a string
print(selfish[::-2])
print(selfish[-1])#print last 1 character from string