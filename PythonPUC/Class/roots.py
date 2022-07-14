a=int(input("co-efficient of x^2:"))
b=int(input("co-efficient of x:"))
c=int(input("constant term:"))
d=(b*b)-(4*a*c)
if(d>0):
	print("REAL ROOTS")
	print("Roots are...",(-b+d**0.5)/2*a,"and",(-b-d**0.5)/2*a)
elif(d==0):
	print("EQUAL ROOTS")
	print("Roots are...",-b/2*a)
else:
	print('IMAGINARY ROOTS..!!')
