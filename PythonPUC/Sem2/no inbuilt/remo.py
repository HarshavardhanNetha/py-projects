l=[1,2,3,'h','hell']
cnt=0
x=0
for i in l:
    x+=1
temp=[]
for i in range(0,x):
    if(type(l[i])==int):
        temp+=[str(l[i])]
    else:        
        temp+=[l[i]]
l2=[]
print(l)
a=input('Element:')
if(a not in temp):
    print('Value is absent.')
else:
    for i in range(0,x):
        if(temp[i]==a and cnt<1):
            cnt+=1
            continue
        else:
            l2+=[l[i]]
    l=l2
    print(l)
