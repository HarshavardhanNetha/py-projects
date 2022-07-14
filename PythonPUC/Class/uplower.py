#Write a program to convert a character lower to upper or upper to lower
a=input("Any Character:")
if(a>="A" and a<="Z"):
	b=a.lower() #converting upper to lower
	print(a,"is Upper. Converted is",b)
else:
	c=a.upper()
	print(a,"is Lower. Converted is",c)
