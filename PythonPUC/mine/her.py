a=int(input('1st side'))
b=int(input('2nd side'))
c=int(input('3rd side'))
s=(a+b+c)/2
print('Area of triangle of sides %d , %d and %d is'%(a,b,c),(s*(s-a)*(s-b)*(s-c))**0.5)
