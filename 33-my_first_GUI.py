#whe 0->blank;when 1->*
#picture->image->pixel
picture=[
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0] 
]
#iterate over picture.
#if 0->print' '
#if 1->print'*'
#use of special parameter "end"
#-->string appended after last value,default a newline
for image in picture:
    for pixel in image:
        if(pixel==1):
            print('*',end='')
        else:
            print(' ',end='')
    print('')


# what is clean good code?
# CLEAN-we make sure everyline we has is readable ans no extra things are added
#READABILITY-proper commenting where needed so that if you see it again or other person sees it is easy for user to understand
#PREDICTABILITY-code should be predictable
#DRY-Dont Repeate Yourself-dont constantly repeat code 
fill='$'
empty=' '
for image in picture:
    for pixel in image:
        if(pixel):
            print(fill,end='')
        else:
            print(empty,end='')
    print('')
