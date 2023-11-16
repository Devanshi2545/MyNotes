is_magician=True
is_expert=False

if is_expert and is_magician:
    print("you are master magician")
    
elif is_magician and not is_expert:
    print("at least you are getting there")

elif not is_magician:
    print("you need magic power")