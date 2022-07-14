#wap to calculate sum of nth digit from fobonacci series
# 0 1 1 2 3 4 5 8 13 ......
def fib(n):
    if(n==1 or n==0):
    #if(n<=1):
        return n
    else:
        return fib(n-1)+fib(n-2)
n=int(input())
print(fib(n))
for i in range(0,n+1):
    print(fib(i),end=" ")
'''l=[]
l.append(fib(n))
print(l)'''
