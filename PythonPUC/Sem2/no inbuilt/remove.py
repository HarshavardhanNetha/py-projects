#remove
l=[]
l2=[]
x=int(input('Enter Size:'))
for i in range(x):
    y=int(input())
    l=l+[y]
cnt=0
a=int(input('Element:'))
#b=int(input('Index:'))
if(a not in l):
    print('Value is absent.')
else:
    for i in range(0,x):
        if(l[i]==a and cnt<1):
            cnt+=1
            continue
        else:
            l2+=[l[i]]
    l=l2
    print(l)
