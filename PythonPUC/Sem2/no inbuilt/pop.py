#pop
l=[]
l2=[]
x=int(input('Enter Size:'))
for i in range(x):
    y=int(input())
    l=l+[y]
a=int(input('Index:'))
if(a>x):
    print('Index out of Range.')
else:
    for i in range(0,x):
        if(i!=a):
            l2+=[l[i]]
    l=l2
    print(l2)
