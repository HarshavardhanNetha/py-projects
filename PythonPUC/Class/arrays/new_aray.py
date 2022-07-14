#pair of genuine 7 is 1 or more
'''7 7 1 t
7 1 7 f
7 7 7 7 1 2 t
7 7 7 f
7 1 7 f
7 7 1 7 1 7 f
1 7 7 1 1 t
71777 f
'''
import array
a=int(input('Size:'))
b=array.array('i',[])
for i in range(a):
    x=int(input())
    b.append(x)
print(b)
x=0
b.append(0)
cnt=0

if(b.count(7)%2==0):
    while(x<len(b)):
        if(b[x]==7 and b[x+1]==7 and b[x+2]!=7):
            cnt+=1
            x+=2
        elif(b[x]==7 and b[x+1]==7 and b[x+1]==7):
            #cnt+=1
            x+=2
        else:
            x+=1
#print(cnt)
if(cnt>=1):
    #if(cnt>b.count(7)%2):
    print('True')
elif(b.count(7)%2!=0):
    print('False')
else:
    print('False')
