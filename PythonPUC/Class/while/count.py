print('Enter -1 to exit...')
pos_count=neg_count=zeroes=0
while(1):
	a=int(input('Enter a number:'))
	if(a==-1):
		break
	elif(a>0):
		pos_count+=1
	elif(a<0):
		neg_count+=1
	else:
		zeroes+=1
print('Count of postive values is',pos_count)
print('Count of negative values is',neg_count)
print('Count of zeroes is',zeroes)
