#armstrong
a=int(input('Enter a number:'))
b=a
sum=0
while(a>0):
	c=a%10
	sum+=c**3
	a//=10
if(sum==b):
	print('Armstrong')
else:
	print('Not Armstrong')
