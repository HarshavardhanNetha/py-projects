a=int(input("Any Number:"))
count=0
n=1
if(n>a):
	if(a%n=0):
		count=count+1
	else:
		n=n+1
else:
	if(count>2):
		print('Not Prime')
	else:
		print("Prime")
