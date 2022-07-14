#wap function that accepts string and calculate upper and lowercase chars
def up_low(s):
    up=low=0
    for i in s:
        if(i.isupper()):
            up+=1
        if(i.islower()):
            low+=1
    print('Upper = {} and Lower = {}'.format(up,low))
