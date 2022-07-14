a=[1,2,3,4,5]
b=[]
x=0
for i in a:
    x+=1
for j in range(1,x+1):
    b=b+[a[-j]]
print(b)
