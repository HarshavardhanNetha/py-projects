a=input()
x=input('Enter char:')
b=a.split(x,1)
y=b[1].replace(x,'$')
c=b[0]+x+y
print(c)
