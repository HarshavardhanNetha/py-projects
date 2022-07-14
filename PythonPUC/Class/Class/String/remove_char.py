#wap to remove nth index char from given string
a=input('Enter string:')
n=int(input('Enter index:'))
if(len(a)>n):
    a1=a[0:n]
    a2=a[n+1:]
    print(a1+a2)
else:
    print('Index is out of bound.')
