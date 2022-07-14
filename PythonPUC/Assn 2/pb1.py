a=input('Gender...')
b=int(input('Salary...'))
c=5*b/100
d=10*b/100
e=3*b/100
if(a=="Male"):
	if(b<10000):
		print("Salary to be paid is %d"%(b+c+e))
	else:
		print("Salary to be paid is %d"%(b+c))
else:
	if(b<10000):
		print("Salary to be paid is %d"%(b+d+e))
	else:
		print("Salary to be paid is %d"%(b+d))
