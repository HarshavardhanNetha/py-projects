a=int(input("Value 1:"))
b=int(input("Value 2:"))
c=int(input("value 3:"))
while(a>b):
	if(a>c):
		print("a is Largest")
	else:
		print("c is Largest")
	break
while(b>c):
	print("b is Largest")
	break
else:
	print("c is Largest")	

