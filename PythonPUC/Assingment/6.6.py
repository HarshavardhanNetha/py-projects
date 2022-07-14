a='He is Ashrith watching me from the window'
b=a.split()
x=0
for i in b:
    if(len(i)>x):
        x=len(i)
        c=i
print(' The largest string : {} \n Length : {}'.format(c,x))
