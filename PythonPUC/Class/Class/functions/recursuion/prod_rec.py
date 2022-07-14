n=int(input())
def prod_rec(n):
    'sum of the squares'
    if(n==1):
        return n
    else:
        return n*n+prod_rec(n-1)
print(prod_rec(n))
