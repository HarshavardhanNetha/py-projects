#read an aarray from the user bu using user defined size and user defined inputs
#find the pair of 7 print True is 7 pair is found else false and even if  7 7 7 
1,7,7 - True
7,7,1 - True
import array
a=int(input('Size:'))
b=array.array('i',[])
for i in range(a):
    x=int(input())
    b.append(x)
print(b)
'''for j in range(a-1):
    if(b[j-1]==7 and b[j]==b[j-1] and b[j]!=b[j+1]):
        print('True')
    else:
        print('False')
'''
cnt=0
for i in range(a-1):
    if(b[i]==7 and b[i+1]==7):
        cnt+=1
if(cnt==1):
    print('True')
else:
    print('False')
