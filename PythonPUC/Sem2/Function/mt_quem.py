x=1
r=2
i=0
n=int(input('Range:'))
def series(i,n):
    x=1*2**i
    if(x<=n):
        print(x,end=' ')
        series(i+1,n)
series(i,n)
#DUB0670242
