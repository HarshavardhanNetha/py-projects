a=int(input())
def fact_rec(a):
    if(a==1):
        return a
    return a*fact_rec(a-1)

print(fact_rec(a))
