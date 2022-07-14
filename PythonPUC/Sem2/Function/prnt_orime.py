n=int(input())

def prime_until_n(n):
    for i in range(2,n+1):
        cnt=0
        for j in range(2,(i//2)+1):
            if(i%j==0):
                cnt=1
                break
        if(cnt==0):
            print(i,end=" ")
prime_until_n(n)
