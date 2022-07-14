n=int(input('How many numbers....??'))
a=1
def pr(a):
    cnt=0
    for i in range(2,(a//2)+1):
        if(a%i==0):
            cnt=1
            break
        if(cnt==0):
            return True
        else:
            return False
def prime(a,n):
    if(pr(a)):
        return prime(a+1,n-1)
    return prime(a+1,n)

print(prime(a,n))
