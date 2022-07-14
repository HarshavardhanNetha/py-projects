#prime or composite
a=int(input('Number:'))
c=0
for i in range(1,a+1):
	if(a%i==0):
		c+=1
if(c>2):
	print('{} is composite'.format(a))
else:
	print('%d is prime'%(a))
