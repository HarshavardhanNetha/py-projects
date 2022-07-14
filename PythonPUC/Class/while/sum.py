#sum of numbers
n=int(input('Number:'))
sum=0
while(n>0):
	dig=n%10
	sum+=dig
	n//=10
print('Sum of numbers is:',sum)
	
