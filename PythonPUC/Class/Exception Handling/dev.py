#wap to divide two numbers by using exception handling
a=int(input())
b=int(input())
try:
    c=a/b
except:
    print('Division with zero')
else:
    print(c)
