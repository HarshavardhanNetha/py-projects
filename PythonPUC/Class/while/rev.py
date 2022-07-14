#reverse number
a=int(input('Number'))
while(a>0):
	a%=10
	print(a,end='')
	a//=10
