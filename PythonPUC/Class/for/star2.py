size = int(input('Enter size : '))
for i in range(1, size):
	for j in range(1,size):
		if(i==1 or i==(size-1) or j==1 or j==(size-1)):
			print('*',end= ' ')
		else:
			print(' ',end = ' ')
	print('\n')
