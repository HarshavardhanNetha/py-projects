a=1
while(a<=999):
	rev=0
	rem=a%10
	rev=rev+(rem**3)
	a/=10
	a+=1
	if(rev==a):
		print(rev)