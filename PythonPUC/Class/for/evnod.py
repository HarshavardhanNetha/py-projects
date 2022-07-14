#wap to even and odd
a=int(input('Starting number:'))
b=int(input("Ending Number:"))
for m in range(a,b+1):
	if(m%2==0):
		print(m,'is even.')
	else:
		print(m,'is odd.')
