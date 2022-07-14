a=input("Any Character:")
num=0
up=0
low=0
while(a!="*"):
	a=input("Any Character:")
	if(a>="0" and a<="9"):
		num+=1
	elif(a>="a" and a<="z"):
		low+=1
	elif(a>="A" and a<="Z"):
		up+=1
print("No of Nums is",num)
print("No of lower case",low)
print("No of upper case",up)
