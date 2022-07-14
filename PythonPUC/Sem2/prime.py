n=int(input())
cnt=0
for i in range(2,(n//2)+1):
    if(n%i==0):
        cnt=1
        break
if(cnt==0):
    print("Prime")
else:
    print('NotPrime')
