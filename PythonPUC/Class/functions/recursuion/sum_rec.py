n=int(input())
def sum_rec(n):
    'sum of the numbers'
    if(n==1):
        return n
    else:
        return n+sum_rec(n-1)
print(sum_rec(n))
