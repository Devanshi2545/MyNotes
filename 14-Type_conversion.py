name="Devanshi"
age=21
relationship='single'

relationship='committed'
print(relationship)
#let try input method taking input from users...
birth_year=input('what year were you born?')
print(birth_year)
#print(type(birth_year))
#if we want to find out our age we need to dubtract it from present year but it id not poosible because by default it is string type
# so we have to convert it into int form
#simply writing int in front of birth_year while subtracting 
#writing int after starting bracket of input
age=2023-int(birth_year)
print(f'your age is: {age}')
