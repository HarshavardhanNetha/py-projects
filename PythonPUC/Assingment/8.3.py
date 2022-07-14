def fib(a):
    if(a<=1):
        return a
    else:
        return fib(a-1)+fib(a-2)
a=int(input())
for i in range(1,a+1):
    print(fib(i),end=' ')
