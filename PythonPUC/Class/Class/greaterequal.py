a=int(input("Num1:"))
b=int(input("Num2:"))
c=int(input("Num3:"))
if(a>b):
	if(a>c):
		print("Num1 is greater")
	else:
		print("Num3 is greater")
elif(b>c):
	print("Num2 is greater")
elif(c>a):
	print("Num3 is greater")
else:
	print("All are equal")
