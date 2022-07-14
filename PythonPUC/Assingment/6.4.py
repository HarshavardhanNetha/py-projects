a='my name my is name foo doo foo me my name'
b=a.split()
print(b)
c=[]
for i in b:
    if i not in c:
        c.append(i)
        print(i,'occured',a.count(i),'times.')
print(c)
print(type(b))
type(c)
#Error - me has occured only once but its showing 4 times
