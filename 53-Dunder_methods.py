class Toy():
    def __init__(self,color,age):
        self.color=color
        self.age=age
        self.my_dict={'name':'victor','has_pets':False}
        
    def __str__(self): #here we modified things not str will return the color
        return f'{self.color}'
    
    def __len__(self): # here changing meaning of the length...
        return 5 # instead of returning the length it would return the number 5
    def __call__(self): #gives the super power to object to call itself
        print('yes??')
        
    def __getitem__(self,i):
        return self.my_dict[i]
        
action_figure=Toy('red',0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure()) # due to __call_- function
#OPTIONAL- read python documentation-->dunder methods
print(action_figure['name'])
 

