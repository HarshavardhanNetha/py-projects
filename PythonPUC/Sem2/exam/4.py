a=int(input())
def fact(a):
    fat=1
    for i in range(1,a+1):
        fat*=i
    return fat
print(fact(a))
