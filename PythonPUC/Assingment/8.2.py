def gcd(a,b):
    x=a%b
    if(x==0):
        print(x)
    else:
        return gcd(x,a)
a=int(input())
b=int(input())
if(a>b):
    gcd(a,b)
else:
    gcd(b,a)
