#read a number from the user print factorial of given number using function
def function(a):
    if(a==1):
        return a
    return a*function(a-1)
a=int(input())
print(function(a))


def facto(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
b=int(input())
print(facto(b))
x=facto(5)
print(x)
