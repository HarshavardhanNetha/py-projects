a=int(input('No. of carbon atoms:'))
b=int(input('No of Hydrogen atoms:'))
if(b==2*a+2):
	print('Alkane')
elif(b==2*a):
	print('Alkene')
elif(b==2*a-2):	
	print('Alkyne')
else:
	print('Not any type')
if(b!=2*a+2):
	a1=str(input("Is that cyclic...[y/n]"))
	if(a1=='y'):
		b1=int(input("No of pi electrons:"))	
		l=[2,6,10,14,18,22,26,30]
		if(b1 in l):
			print('Aromatic')
		else:
			print('Not Aromatic')
	else:
		print('Not Aromatic')
else:
	print('Not aromatic')
