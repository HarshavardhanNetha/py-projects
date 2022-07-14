str= "Welcome to the RGUKT Basar Campus and Python Programming"
print(str[9])
print(str[-1::-1])
print(str.split())
for i in str:
    if(i>='A' and i<='Z'):
        print(i,end=" ")
print()
print(len(str))
c=''
for i in str:
    b=i.capitalize()
    print(b,end='')
print(c)
b=str.split()
for i in b:
    if(i=='RGUKT'):
        print(b[i])
