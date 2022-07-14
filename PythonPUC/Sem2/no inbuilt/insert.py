#insert
l=[]
l2=[]
x=int(input('Enter Size:'))
for i in range(x):
    y=int(input())
    l=l+[y]
a=int(input('Element:'))
b=int(input('Index:'))
if(b>x-1):
    l=l+[a]
else:
    for i in range(0,b):
        l2+=[l[i]]
    l2+=[a]
    for i in range(b,x):
        l2+=[l[i]]
l=l2
print(l)
