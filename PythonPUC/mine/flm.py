a1=input()
b1=input()
a=list(a1)
b=list(b1)
c=a
d=b
for i in a:
    if(i in b):
        c.remove(i)
        d.remove(i)
        #print(a,b)
    else:
        continue
print(c,d)
cnt=len(a)+len(b)
print(cnt)
