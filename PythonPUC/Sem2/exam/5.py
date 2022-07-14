a=int(input())
b=int(input())
while(b>a):
    b=int(input('Enter less than {} :'.format(a)))
def gcd(a,b):
    x=a%b
    if(a%b==0):
        return b
    return gcd(b,a%b)
print(gcd(a,b))
