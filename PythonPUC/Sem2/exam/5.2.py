a=int(input())
b=int(input())
while(a%b==0):
    print(b)
else:
    a=b
    b=a%b
