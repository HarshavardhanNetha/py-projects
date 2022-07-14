a=input('Comma seperated Values:')
b=a.split(',')
c=[]
for i in b:
    c.append(i)
print(c)
print(tuple(c))
