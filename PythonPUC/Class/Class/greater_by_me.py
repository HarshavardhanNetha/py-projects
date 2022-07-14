a=int(input("Num1:"))
b=int(input("Num2:"))
c=int(input("Num3:"))
if(a==b==c):
	print("a,b and c are equal")

	if(a==b):
		print("a and b are equal")
	if(a==c):
		print("a and c are equal")
	if(b==c):
		print("b and c are equal")
elif(a>b):
	if(a>c):
		print("Num1 is greater")
	else:
		print("Num3 is greater")
else:
	if(b<c):
		print("Num3 is greater")
	else:
		print("Num2 is greater")

