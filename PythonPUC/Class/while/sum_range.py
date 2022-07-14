#sum od numbers in given range
m=int(input('Begining:'))
m1=m
n=int(input('End:'))
sum=0
while(m<=n):
	sum+=m
	m+=1
print('Sum of numbers from %d to %d is %d'%(m1,n,sum))
