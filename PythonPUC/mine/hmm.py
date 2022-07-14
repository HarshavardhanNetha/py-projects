n=1
for n in range(1,9999):
	rev=0
	while(n>0):
		rem=n%10
		rev=rev+(rem*rem*rem)
		n//=10
	if(rev==n):
		print(n)
	n+=1
n=0
