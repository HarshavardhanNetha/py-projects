n=int(input('Enter a value:'))
sum=0
for n in range(1,n+1):
	sum+=n
print('Avg of {} numbers is {}'.format(n,sum/n))
