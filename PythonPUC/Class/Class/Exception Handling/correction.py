#wap to divide two numbers by using exception handling
a=int(input())
b=int(input())
while(True):
    try:
        c=a/b
    except:
        print('Division with zero')
        b=int(input("enter denom"))
    else:
        print(c)
        break
