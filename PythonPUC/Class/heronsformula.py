a=int(input("1st side:"))
b=int(input("2nd side:"))
c=int(input("3rd side:"))
print(a,b,c)
s=(a+b+c)/2
#print(s)
print("Area of the triangle of sides {},{} and {} is".format(a,b,c),(s*(s-a)*(s-b)*(s-c))**0.5)
