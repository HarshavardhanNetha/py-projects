a=input('The sequence of caps....')
b=list(a)
#print(b)
cnt_f=cnt_b=0
e=[]
x=0
for i in range(1,len(b)):
    if(b[x]!=b[i]):
        e.append((x,i-1,b[x]))
        if(a[x]=='F'):
            cnt_f+=1
        else:
            cnt_b+=1
        x=i
#print(cnt_f,cnt_b)
if(cnt_f<cnt_b):
    flip='F'
else:
    flip='B'
for j in e:
    if(j[2]==flip):
        print('People in position {} throungh {} flip your caps.'.format(j[0],j[1]))
