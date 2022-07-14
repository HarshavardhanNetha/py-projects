#creating dict with user inputs
a={}
while(1):
	i=input('key')
	if(i=="end"):
		break
	else:
		j=input('value')
		a[i]=j
#i is key j is value
print(a)
