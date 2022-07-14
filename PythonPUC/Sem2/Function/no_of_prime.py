n=int(input())
def no_of_primes(n):
    prime_cnt=0
    null=2
    while(prime_cnt<n):
        cnt=0
        for j in range(2,(null//2)+1):
            if(null%j==0):
                cnt=1
                break
        if(cnt==0):
            print(null,end=" ")
            prime_cnt+=1
        null+=1
no_of_primes(n)
