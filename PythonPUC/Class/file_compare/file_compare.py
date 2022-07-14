#wap to compare two files
with open('me.txt') as f:
	with open('2.txt') as g:
		a=f.read()
		b=g.read()
		if(a==b):
			print('Equal')
