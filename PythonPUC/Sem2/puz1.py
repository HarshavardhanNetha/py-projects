t=input('Series of caps(F for forward and B for backward):')
a=list(t)
a.append('END')
fc=bc=0
f=[]
b=[]
if(t[0]=='F'):
    f.append(0)
else:
    b.append(0)
#print(f,b)
for i in range(len(a)-1):
    if(a[i]!=a[i+1]):
        if(a[i]=='F'):
            fc+=1
            f.append(i)
            if(a[i+1]=='B'):
                b.append(i+1)
        else:
            bc+=1
            b.append(i)
            if(a[i+1]=='F'):
                f.append(i+1)
#print(fc,bc)
#print(f)
#print(b)
if(fc<bc):
    for i in range(len(f)-1):
        if(i%2==0):
            print('Person(s) in position(s) {} to {} flip your cap.'.format(f[i],f[i+1]))
else:
    for i in range(len(b)-1):
        if(i%2==0):
            print('Person(s) in position(s) {} to {} flip your cap.'.format(b[i],b[i+1]))
