#input a number print factorial of numberusing recursion
def fact(a):
    if(a==0):
        return 1
    return a*fact(a-1)
x=int(input())
print(fact(x))
