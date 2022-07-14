a=int(input("Num1:"))
b=int(input("Num2:"))
c=int(input("Num3:"))
if(a>b)and(a>c):
	print("a is large")
elif(a<c)and(b<c):
	print("c is greater")
else:
	print("b is greater")
