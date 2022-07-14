a=int(input())
for i in range(1,a+1):
	print()
	for j in range(1,i-1):
		print('*',end='')
for i in range(a,1,-1):
	print()
	for j in range(i,1,-1):
		print('*', end = '')
print()
'''while(a>0):
	print()
	print('*'*a,end='')
	a-=1
print()'''
