a=int(input())
b=int(input())
c=int(input())
if(a==b):
    if(a==c):
        print('All are equal')
    else:
        print('a and b are equal')
elif(a==c):
    if(a==b):
        print('All are equal')
    else:
        print('A AND CARE EQUAL')
if(a>b):
    if(a>c):
        print(a)
    else:
        print(c)
elif(b>a):
    if(b>c):
        print(b)
    else:
        print(c)
