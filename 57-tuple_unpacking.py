#with a for loop
stock_prices= [('apple',200),('google',400),('MSFt',600)]

for item in stock_prices:
    print(item)
    
for item,prices in stock_prices:
    print(item)
    print(prices)
    
#lets do it with a function

work_hours=[('abby',100),('billy',4000),('cassie',800)]
def employ_check(work_hours):
    current_max=0
    employ_of_the_month=''
    
    for employee,hours in work_hours:
        if hours>current_max:
            current_max=hours
            employ_of_the_month=employee
        else:
            pass
        
    return (employ_of_the_month,current_max)

print(employ_check(work_hours))

name,hours=employ_check(work_hours)
print(name)
