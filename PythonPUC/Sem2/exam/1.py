a=int(input())
sum=0
for i in range(1,a+1):
    fact=1
    for j in range(1,i+1):
            fact*=j
    sum+=i/fact
print(sum)
